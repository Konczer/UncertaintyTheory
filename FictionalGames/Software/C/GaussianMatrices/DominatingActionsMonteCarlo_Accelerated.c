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
 * $ gcc DominatingActionsMonteCarlo_Accelerated.c -lm
 * $ gcc DominatingActionsMonteCarlo_Accelerated.c -lm -O3
 * $ gcc DominatingActionsMonteCarlo_Accelerated.c -lm -O3 -o DominatingActionsMonteCarlo_Accelerated
 * Using g++
 * $ g++ DominatingActionsMonteCarlo_Accelerated.c -lm
 * $ g++ DominatingActionsMonteCarlo_Accelerated.c -lm -O3
 * $ g++ DominatingActionsMonteCarlo_Accelerated.c -lm -O3 -o DominatingActionsMonteCarlo_Accelerated
 * 
 * Usage:
 * DominatingActionsMonteCarlo_Accelerated N M n_max [seed] [rand_type]
 * 
 * Examples:
 * $ ./DominatingActionsMonteCarlo_Accelerated 4 6 1000000 2025
 * $ 4408
 * 
 * $ ./DominatingActionsMonteCarlo_Accelerated 5 6 1000000 2025
 * $ 770
 * 
 * $ ./DominatingActionsMonteCarlo_Accelerated 4 6 1000000 2025 "rand"
 * $ 4408
 * 
 * $ ./DominatingActionsMonteCarlo_Accelerated 5 6 1000000 2025 "rand"
 * $ 770
 * 
 * $ ./DominatingActionsMonteCarlo_Accelerated 4 6 1000000 2025 "drand48"
 * $ 4381
 * 
 * $ ./DominatingActionsMonteCarlo_Accelerated 5 6 1000000 2025 "drand48"
 * $ 762
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

// Macro to generate the Maximum of two Gaussian random number using a modified Box-Muller transform
#define GENERATE_GAUSSIAN_TWOMAX(result) { \
    double u1 = ((double) rand() / RAND_MAX); \
    double u2 = ((double) rand() / RAND_MAX); \
    result = sqrt(-2.0 * log(u1)) * sin(M_PI * (u2 + 0.25)); \
}

// Macro to generate the Maximum of two Gaussian random number using a modified Box-Muller transform
#define GENERATE_GAUSSIAN_TWOMAX_DRAND48(result) { \
    double u1 = drand48(); \
    double u2 = drand48(); \
    result = sqrt(-2.0 * log(u1)) * sin(M_PI * (u2 + 0.25)); \
}


// Dominance check function for even N (N = 2 * K)
int dominance_check_even(int M, int N_half) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using the Box-Muller transform
        GENERATE_TWO_GAUSSIANS(X, Y);

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        GENERATE_GAUSSIAN_TWOMAX(Z);
        for (k = 1; k < N_half-1; k++) {
            double Zi;
            GENERATE_GAUSSIAN_TWOMAX(Zi);
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

// Dominance check function for odd N (N = 2 * K + 1)
int dominance_check_odd(int M, int N_half_ceil) {
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
        for (k = 1; k < N_half_ceil-1; k++) {
            double Zi;
            GENERATE_GAUSSIAN_TWOMAX(Zi);
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


// Dominance check function for even N (N = 2 * K) with drand48
int dominance_check_even_drand48(int M, int N_half) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using the Box-Muller transform
        GENERATE_TWO_GAUSSIANS_DRAND48(X, Y);

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        GENERATE_GAUSSIAN_TWOMAX_DRAND48(Z);
        for (k = 1; k < N_half-1; k++) {
            double Zi;
            GENERATE_GAUSSIAN_TWOMAX_DRAND48(Zi);
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


// Dominance check function for odd N (N = 2 * K + 1) with drand48
int dominance_check_odd_drand48(int M, int N_half_ceil) {
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
        for (k = 1; k < N_half_ceil-1; k++) {
            double Zi;
            GENERATE_GAUSSIAN_TWOMAX_DRAND48(Zi);
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

    
    if (N % 2 == 0) {
        if (strcmp(rng_type, "drand48") == 0) {
            // Run the dominance check function n_max times
            result = 0; for (i = 0; i < n_max; i++) {result += dominance_check_even_drand48(M, N / 2);} 
        } else {
            // Run the dominance check function n_max times
            result = 0; for (i = 0; i < n_max; i++) {result += dominance_check_even(M, N / 2);}
        }
    } else {
        if (strcmp(rng_type, "drand48") == 0) {
            // Run the dominance check function n_max times
            result = 0; for (i = 0; i < n_max; i++) {result += dominance_check_odd_drand48(M, N / 2 + 1);} // Integer division  
        } else {
            // Run the dominance check function n_max times
            result = 0; for (i = 0; i < n_max; i++) {result += dominance_check_odd(M, N / 2 + 1);} // Integer division 
        }
    }

    
    printf("%d\n", result);
    return 0;
}


