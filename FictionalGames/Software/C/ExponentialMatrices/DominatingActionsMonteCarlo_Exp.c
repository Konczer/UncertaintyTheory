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
 * $ gcc DominatingActionsMonteCarlo_Exp.c -lm
 * $ gcc DominatingActionsMonteCarlo_Exp.c -lm -O3
 * $ gcc DominatingActionsMonteCarlo_Exp.c -lm -O3 -o DominatingActionsMonteCarlo_Exp
 * Using g++
 * $ g++ DominatingActionsMonteCarlo_Exp.c -lm
 * $ g++ DominatingActionsMonteCarlo_Exp.c -lm -O3
 * $ g++ DominatingActionsMonteCarlo_Exp.c -lm -O3 -o DominatingActionsMonteCarlo_Exp
 * 
 * Usage:
 * DominatingActionsMonteCarlo_Exp N M n_max [seed] [rand_type]
 * 
 * Example:
 * $ ./DominatingActionsMonteCarlo_Exp 4 6 1000000 2025
 * $ 6680
 * 
 * $ ./DominatingActionsMonteCarlo_Exp 4 6 1000000 2025 "rand"
 * $ 6680
 * 
 * $ ./DominatingActionsMonteCarlo_Exp 4 6 1000000 2025 "drand48"
 * $ 6636
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>


// Dominance check function
int dominance_check(int M, int N) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y uniform random variables
        X = -log((double) rand() / RAND_MAX); \
        Y = -log((double) rand() / RAND_MAX); \

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        Z = -log((double) rand() / RAND_MAX);
        for (k = 1; k < N-2; k++) {
            double Zi;
            Zi = -log((double) rand() / RAND_MAX);
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
        X = -log(drand48()); \
        Y = -log(drand48()); \

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        Z = -log(drand48()); \
        for (k = 1; k < N-2; k++) {
            double Zi;
            Zi = -log(drand48()); \
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


