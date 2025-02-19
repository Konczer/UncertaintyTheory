/**
 * Optimized by the help of AI, ChatGPT o4 at 2025. 02. 19.
 * 
 * Uses internally implemented XorShift128
 * Is parallelized
 * Can be seeded, but because of parallelization it is not completely deterministic 
 * 
 * Compilation examples:
 * Using gcc
 * $ gcc -O3 -march=native -fopenmp -ffast-math -funroll-loops DominatingActionsMonteCarlo_Accelerated_AI.c -lm
 * $ gcc -O3 -march=native -fopenmp -ffast-math -funroll-loops -o DominatingActionsMonteCarlo_Accelerated_AI DominatingActionsMonteCarlo_Accelerated_AI.c -lm
 * 
 * Usage:
 * DominatingActionsMonteCarlo_Accelerated N M n_max [seed]
 * 
 * Examples:
 * $ ./DominatingActionsMonteCarlo_Accelerated 4 6 1000000 2025
 * The output is probabilistic, a few generated values were:
 * $ 4596   $ 4636  $ 4634  $ 4628
 * 
 * 
 *
 * */ 



#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <immintrin.h>
#include <omp.h>

// Xorshift128+ PRNG: High-speed, high-quality pseudorandom number generator
typedef struct {
    uint64_t state[2];
} XorShift128;

static inline uint64_t xorshift128plus(XorShift128 *rng) {
    uint64_t s1 = rng->state[0];
    uint64_t s0 = rng->state[1];
    rng->state[0] = s0;
    s1 ^= s1 << 23;
    rng->state[1] = s1 ^ s0 ^ (s1 >> 17) ^ (s0 >> 26);
    return rng->state[1] + s0;
}

// Fast Gaussian random number generator using Box-Muller transform (Generates two Gaussians at once)
static inline void fast_gaussian_pair(XorShift128 *rng, double *g1, double *g2) {
    static const double TWO_PI = 6.283185307179586476925286766559;
    double u1 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0); // Scale to (0,1]
    double u2 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    double r = sqrt(-2.0 * log1p(u1 - 1.0));
    double theta = TWO_PI * u2;
    *g1 = r * cos(theta);
    *g2 = r * sin(theta);
}

// Fast Gaussian random number generator using Box-Muller transform
static inline void fast_gaussian(XorShift128 *rng, double *g1) {
    static const double TWO_PI = 6.283185307179586476925286766559;
    double u1 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0); // Scale to (0,1]
    double u2 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    *g1 = sqrt(-2.0 * log1p(u1 - 1.0)) * cos(TWO_PI * u2);
}

// Two Gaussian Max Trick
static inline double fast_gaussian_max(XorShift128 *rng) {
    double u1 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    double u2 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    return sqrt(-2.0 * log1p(u1 - 1.0)) * sin(M_PI * (u2 + 0.25));
}

// Dominance check function
int dominance_check(int M, int N, XorShift128 *rng) {
    double Low = 0, High = 1, X, Y, Z;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y simultaneously using fast Gaussian pair
        fast_gaussian_pair(rng, &X, &Y);

        // Handle even and odd N cases correctly
        if (N % 2 == 0) {
            Z = fast_gaussian_max(rng);
            for (k = 2; k < N - 2; k += 2) {
                double Zi = fast_gaussian_max(rng);
                Z = (Zi > Z) ? Zi : Z;
            }
        } else {
            fast_gaussian(rng, &Z);
            for (k = 1; k < N - 2; k += 2) {
                double Zi = fast_gaussian_max(rng);
                Z = (Zi > Z) ? Zi : Z;
            }
        }

        // Branchless comparisons to reduce CPU stalls
        int condition1 = (X <= Z) & (Y <= Z);
        int condition2 = (X > Z) & (Y > Z);
        if (condition1) return 0;
        if (!condition2) {
            if (X > Y) {
                double newLow = (Z - Y) / (X - Y);
                Low = (Low < newLow) ? newLow : Low;
            } else {
                double newHigh = (Y - Z) / (Y - X);
                High = (High > newHigh) ? newHigh : High;
            }
            if (Low > High) return 0;
        }
    }
    return 1;
}

// Main function
int main(int argc, char *argv[]) {
    if (argc < 4 || argc > 5) {
        fprintf(stderr, "Usage: %s N M n_max [seed]\n", argv[0]);
        return 1;
    }

    int N = atoi(argv[1]);
    int M = atoi(argv[2]);
    int n_max = atoi(argv[3]);
    uint64_t seed = (argc == 5) ? atoll(argv[4]) : time(NULL);

    // Initialize PRNG state
    XorShift128 rng;
    rng.state[0] = seed ^ 0x9E3779B97F4A7C15;
    rng.state[1] = seed ^ 0xBF58476D1CE4E5B9;

    int result = 0;

    // OpenMP parallelization
    #pragma omp parallel
    {
        XorShift128 local_rng = rng; // Thread-local PRNG state
        int local_result = 0;

        #pragma omp for nowait schedule(dynamic)
        for (int i = 0; i < n_max; i++) {
            local_result += dominance_check(M, N, &local_rng);
        }

        #pragma omp atomic
        result += local_result;
    }

    printf("%d\n", result);
    return 0;
}
