/**
 * Uses arc4random() for random number generation, does not allow setting seed
 * https://man.openbsd.org/arc4random
 * https://linux.die.net/man/3/arc4random
 * 
 * Runs on Linux, needs libbsd-dev for the arc4random function
 * 
 * To install libbsd-dev use the following command:
 * $ sudo apt install libbsd-dev
 * 
 * Compilation examples:
 * Using gcc
 * $ gcc DominatingActionsMonteCarlo_arc4random.c -lm -lbsd
 * $ gcc DominatingActionsMonteCarlo_arc4random.c -lm -lbsd -O3
 * $ gcc DominatingActionsMonteCarlo_arc4random.c -lm -lbsd -O3 -o DominatingActionsMonteCarlo_arc4random
 * Using g++
 * $ g++ DominatingActionsMonteCarlo_arc4random.c -lm -lbsd
 * $ g++ DominatingActionsMonteCarlo_arc4random.c -lm -lbsd -O3
 * $ g++ DominatingActionsMonteCarlo_arc4random.c -lm -lbsd -O3 -o DominatingActionsMonteCarlo_arc4random
 * 
 * Usage:
 * DominatingActionsMonteCarlo_arc4random N M n_max
 * 
 * Example:
 * $ ./DominatingActionsMonteCarlo_arc4random 4 6 1000000
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

#include <sys/types.h>
#include <bsd/stdlib.h> // For arc4random on Linux, this needs libbsd-dev, on linux it can be installed: $ sudo apt install libbsd-dev





#define GENERATE_GAUSSIAN_ARC4RANDOM(result) { \
    double u1 = ((double) arc4random() / UINT32_MAX); \
    double u2 = ((double) arc4random() / UINT32_MAX); \
    result = sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2); \
}



#define GENERATE_TWO_GAUSSIANS_ARC4RANDOM(resX, resY) { \
    double r = sqrt(-2.0 * log( ((double) arc4random() / UINT32_MAX) )); \
    double alph = 2.0 * M_PI * ((double) arc4random() / UINT32_MAX); \
    resX = r * cos(alph); \
    resY = r * sin(alph); \
}


// Dominance check function with arc4random
int dominance_check_arc4random(int M, int N) {
    double Low = 0;
    double High = 1;
    double X, Y, Z;
    double u1, u2;
    int j, k;

    for (j = 1; j <= M; j++) {
        // Generate X and Y using the Box-Muller transform
        GENERATE_TWO_GAUSSIANS_ARC4RANDOM(X, Y);

        // Generate Z as the maximum of N-2 independent Gaussian random variables
        GENERATE_GAUSSIAN_ARC4RANDOM(Z);
        for (k = 1; k < N-2; k++) {
            double Zi;
            GENERATE_GAUSSIAN_ARC4RANDOM(Zi);
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
    int N, M, n_max;
    int i, result;
    //const char *rng_type = "arc4random";

    // Check the number of arguments
    if (argc < 4 || argc > 4) {
        fprintf(stderr, "Usage: %s N M n_max\n", argv[0]);
        return 1;
    }

    // Parse the command-line arguments
    N = atoi(argv[1]);
    M = atoi(argv[2]);
    n_max = atoi(argv[3]);

    arc4random_stir();

    result = 0; 
    for (i = 0; i < n_max; i++) {
        result += dominance_check_arc4random(M, N);
    }
    
    printf("%d\n", result);
    return 0;
}


