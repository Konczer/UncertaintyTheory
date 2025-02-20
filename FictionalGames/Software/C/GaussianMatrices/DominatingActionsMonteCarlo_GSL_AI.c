/**
 * Optimized by the help of AI, ChatGPT o4 at 2025. 02. 19.
 * 
 * Uses GNU Scientific Library (GLS)
 * https://www.gnu.org/software/gsl/
 * https://www.gnu.org/software/gsl/doc/latex/gsl-ref.pdf
 * 
 * Uses internally implemented XorShift128
 * Is parallelized
 * Can be seeded, but because of parallelization it is not completely deterministic 
 * 
 * 
 * Compilation examples:
 * Using gcc
 * $ gcc -O3 -march=native -fopenmp -ffast-math -funroll-loops -o DominatingActionsMonteCarlo_GSL_AI DominatingActionsMonteCarlo_GSL_AI.c -lm -lgsl -lgslcblas
 * 
 * Usage:
 * DominatingActionsMonteCarlo_GSL_AI N M n_max [seed]
 * 
 * Examples:
 * $ ./DominatingActionsMonteCarlo_GSL_AI 4 6 1000000 2025
 * The output is probabilistic, a few generated values were:
 * $ 4273   $ 4244  $ 4286  $ 4284
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <gsl/gsl_cdf.h>
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

// Fast Gaussian random number generator using Box-Muller transform
static inline void fast_gaussian_pair(XorShift128 *rng, double *g1, double *g2) {
    static const double TWO_PI = 6.283185307179586476925286766559;
    double u1 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    double u2 = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0);
    double r = sqrt(-2.0 * log1p(u1 - 1.0));
    double theta = TWO_PI * u2;
    *g1 = r * cos(theta);
    *g2 = r * sin(theta);
}

// Macro to generate Z as the maximum of N-2 independent Gaussian random variables using GSL
#define GENERATE_MAX_GAUSSIAN(Z, N, rng) { \
    double U = (xorshift128plus(rng) >> 11) * (1.0 / 9007199254740992.0); \
    Z = gsl_cdf_gaussian_Pinv(pow(U, 1.0 / (N - 2)), 1.0); \
}

// Dominance check function
int dominance_check(int M, int N, XorShift128 *rng) {
    double Low = 0, High = 1, X, Y, Z;
    int j;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using Box-Muller transform
        fast_gaussian_pair(rng, &X, &Y);

        // Generate Z using the GSL-based max Gaussian evaluation
        GENERATE_MAX_GAUSSIAN(Z, N, rng);

        if (X <= Z && Y <= Z) {
            return 0; // False
        } else if (!(X > Z && Y > Z)) {
            if (X > Y) {
                double newLow = (Z - Y) / (X - Y);
                if (Low < newLow) {
                    Low = newLow;
                }
            } else {
                double newHigh = (Y - Z) / (Y - X);
                if (High > newHigh) {
                    High = newHigh;
                }
            }

            if (Low > High) {
                return 0; // False
            }
        }
    }
    return 1; // True
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
