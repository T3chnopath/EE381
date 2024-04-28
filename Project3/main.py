# Import Python standard library modules
import random as rand
import matplotlib.pyplot as plot
import numpy as np

# Import user libraries
from helpers import nsided_die

# Constants
N_TRIALS      = 1000
N_EXPERIMENTS = 10_000


# ---------- PART 1: Experimental Bernoulli Trials ----------
def testBernoulli() -> int:
    successes = 0
    p = [0.30, 0.10, 0.20, 0.25, 0.15]
    successArr = np.empty(N_EXPERIMENTS, dtype=int)

    # Repeat experiment N times
    for i in range(N_EXPERIMENTS):
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
    plot.stem(x_labels, frequencies / N_EXPERIMENTS)
    plot.xticks(x_labels)
    plot.show()    


# ---------- PART 2: Calculations using the Binomial Distribution ----------
def testBinomial():
    x = 3         # Targetting three, 5s in a row
    p = 0.15 ** x # probability of rolling three 5s
    successArr = np.empty(N_EXPERIMENTS, dtype=int)

    # Repeat experiment N times
    for i in range(N_EXPERIMENTS):

        # Perform the binomial distribution 
        outcomes = np.random.choice([0, 1], size=N_TRIALS, p=[1-p, p])
        
        # Count the number of successes (number of 1s) in the outcomes
        num_successes = np.sum(outcomes)
        
        # Store the number of successes for this trial
        successArr[i] = num_successes
    
    # Create frequency map of number of successes 
    frequencies = np.bincount(successArr)
    # Ensure all elements in frequencies are represented on X axis
    x_labels = np.arange(len(frequencies))

    # Plot the PMF of the output array
    plot.title("Bernoulli Trials: PMF - Binomial Formula")
    plot.xlabel("Number of Successes in n = 1000 Trials")
    plot.ylabel("Probability")
    plot.stem(x_labels, frequencies / N_EXPERIMENTS)
    plot.xticks(x_labels)
    plot.show()    


# ---------- PART 3: Approximation of Binomial by Poisson Distribution ----------
def testPoisson():
    counts = []
    x = 3         # Targetting three, 5s in a row
    p = 0.15 ** x # probability of rolling three 5s
    successArr = np.empty(N_EXPERIMENTS, dtype=int)

    # lambda is equal to num trials * prob of success in each
    lamb = N_TRIALS * p

    # Set this to hold up to 100 possible occurences for each trial
    successArr = np.zeros(100, dtype=int)

    # Repeat experiment N times
    for i in range(N_EXPERIMENTS):

        # Outputs array of success for all trials 
        poisson_samples = np.random.poisson(lamb, N_TRIALS)

        # Count the occurrences of each unique value in poisson_samples
        counts = np.bincount(poisson_samples)

        # Add the counts from the current experiment to the total counts
        successArr[:len(counts)] += counts

     # Find the index of the last non-zero element in total_counts
    last_nonzero_index = np.nonzero(successArr)[0][-1]

    # Get the length of the valid portion of the success array
    valid_length = last_nonzero_index + 1

    # Ensure all elements in frequencies are represented on X axis
    x_labels = np.arange(valid_length)

    # Plot the PMF of the output array
    plot.title("Bernoulli Trials: PMF - Poisson Distribution")
    plot.xlabel("Number of Successes in n = 1000 Trials")
    plot.ylabel("Probability")
    plot.stem(x_labels, successArr[:valid_length] / N_EXPERIMENTS)
    plot.xticks(x_labels)
    plot.show()    


def main():
    testBernoulli()
    testBinomial()
    testPoisson()


# Call main if run from the command line
if __name__ == "__main__":
    main()
