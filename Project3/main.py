# Import Python standard library modules
import random as rand
import matplotlib.pyplot as plot
import numpy as np

# Import user libraries
from nsided_die import nsided_die

# Constants
N_TRIALS = 1000

# ---------- PART 1: Experimental Bernoulli Trials ----------
def testBernoilli() -> int:
    successes = 0
    N = 10_000
    p = [0.30, 0.10, 0.20, 0.25, 0.15]
    successArr = np.empty(N, dtype=int)

    # Repeat experiment N times
    for i in range(N):
        successes = 0 

        # Experiment requires n trials 
        for j in range(N_TRIALS):
            dice1 = nsided_die(p)
            dice2 = nsided_die(p)
            dice3 = nsided_die(p)

            if dice1 == dice2 == dice3 == 5:
                successes += 1

        successArr[i] = successes

    # Create frequency map of number of successes 
    frequencies = np.bincount(successArr)

    # Ensure all elements in frequencies are represented on X axis
    x_labels = np.arange(len(frequencies))

    # Plot the PMF of the output array
    plot.title("Bernoulli Trials: PMF - Experimental Results")
    plot.xlabel("Number of Successes in n = 1000 Trials")
    plot.ylabel("Probability")
    plot.stem(x_labels, frequencies / N)
    plot.xticks(x_labels)
    plot.show()    


# Main function is used for desired test cases
def main():
    testBernoilli()


# Call main if run from the command line
if __name__ == "__main__":
    main()
