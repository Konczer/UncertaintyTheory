/**
 * Two pseudo-random generators can be chosed:
 * rand()
 * https://man7.org/linux/man-pages/man3/rand.3.html
 * 
 * drand48()
 * https://man7.org/linux/man-pages/man3/drand48.3.html
 * https://www.ibm.com/docs/en/zos/2.4.0?topic=functions-drand48-pseudo-random-number-generator
 * 
 * Compilation examples:
 * Using gcc
 * $ gcc DominatingActionsMonteCarlo.c -lm
 * $ gcc DominatingActionsMonteCarlo.c -lm -O3
 * $ gcc DominatingActionsMonteCarlo.c -lm -O3 -o DominatingActionsMonteCarlo
 * Using g++
 * $ g++ DominatingActionsMonteCarlo.c -lm
 * $ g++ DominatingActionsMonteCarlo.c -lm -O3
 * $ g++ DominatingActionsMonteCarlo.c -lm -O3 -o DominatingActionsMonteCarlo
 * 
 * Usage:
 * DominatingActionsMonteCarlo N M n_max [seed] [rand_type]
 * 
 * Example:
 * $ ./DominatingActionsMonteCarlo 4 6 1000000 2025
 * $ 4532
 * 
 * $ ./DominatingActionsMonteCarlo 4 6 1000000 2025 "rand"
 * $ 4532
 * 
 * $ ./DominatingActionsMonteCarlo 4 6 1000000 2025 "drand48"
 * $ 4474
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>


// Macro to generate a single Gaussian random number using the Box-Muller transform
#define GENERATE_GAUSSIAN(result) { \
    double u1 = ((double) rand() / RAND_MAX); \
    double u2 = ((double) rand() / RAND_MAX); \
    result = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2); \
}

// Macros for generating Gaussian random numbers using drand48 and arc4random
#define GENERATE_GAUSSIAN_DRAND48(result) { \
    double u1 = drand48(); \
    double u2 = drand48(); \
    result = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2); \
}


// Macro to generate a single Gaussian random number using the Box-Muller transform
#define GENERATE_TWO_GAUSSIANS(resX, resY) { \
    double r = sqrt(-2.0 * log( ((double) rand() / RAND_MAX) )); \
    double alph = 2.0 * M_PI * ((double) rand() / RAND_MAX); \
    resX = r * cos(alph); \
    resY = r * sin(alph); \
}

// Macros for generating Gaussian random numbers using drand48 and arc4random
#define GENERATE_TWO_GAUSSIANS_DRAND48(resX, resY) { \
    double r = sqrt(-2.0 * log( drand48())); \
    double alph = 2.0 * M_PI * ( drand48()); \
    resX = r * cos(alph); \
    resY = r * sin(alph); \
}

// Dominance check function
int dominance_check(int M, int N) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using the Box-Muller transform
        GENERATE_TWO_GAUSSIANS(X, Y);

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        GENERATE_GAUSSIAN(Z);
        for (k = 1; k < N-2; k++) {
            double Zi;
            GENERATE_GAUSSIAN(Zi);
            if (Zi > Z) {
                Z = Zi;
            }
        }

        if (X <= Z && Y <= Z) {
            return 0; // False
        } else if (!(X > Z && Y > Z)) {
            if (X > Y) {
                double newLow = (Z - Y) / (X - Y);
                if (Low < newLow) {
                    Low = newLow;
                    }
            } else if (X < Y) {
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

// Dominance check function with drand48
int dominance_check_drand48(int M, int N) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using the Box-Muller transform
        GENERATE_TWO_GAUSSIANS_DRAND48(X, Y);

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        GENERATE_GAUSSIAN_DRAND48(Z);
        for (k = 1; k < N-2; k++) {
            double Zi;
            GENERATE_GAUSSIAN_DRAND48(Zi);
            if (Zi > Z) {
                Z = Zi;
            }
        }

        if (X <= Z && Y <= Z) {
            return 0; // False
        } else if (!(X > Z && Y > Z)) {
            if (X > Y) {
                double newLow = (Z - Y) / (X - Y);
                if (Low < newLow) {
                    Low = newLow;
                    }
            } else if (X < Y) {
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


int main(int argc, char *argv[]) {
    int N, M, n_max, seed;
    int i, result;
    const char *rng_type = "rand";

    // Check the number of arguments
    if (argc < 4 || argc > 6) {
        fprintf(stderr, "Usage: %s N M n_max [seed] [rand_type]\n", argv[0]);
        return 1;
    }

    // Parse the command-line arguments
    N = atoi(argv[1]);
    M = atoi(argv[2]);
    n_max = atoi(argv[3]);

    if (argc >= 5) {
        seed = atoi(argv[4]);
    } else {
        seed = time(NULL);
    }

    srand(seed);
    srand48(seed);

    if (argc == 6) {
        rng_type = argv[5];
    }

    

    if (strcmp(rng_type, "drand48") == 0) {
        // Run the dominance check function n_max times
        result = 0; for (i = 0; i < n_max; i++) {result += dominance_check_drand48(M, N);} 
    } else {
        // Run the dominance check function n_max times
        result = 0; for (i = 0; i < n_max; i++) {result += dominance_check(M, N);}
    }
    
    printf("%d\n", result);
    return 0;
}


