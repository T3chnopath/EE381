# Import Python standard library modules
import random as rand
import matplotlib.pyplot as plot
import numpy as np

from math import log10, isclose

# Import user modules
from nsided_die import nsided_die
from cards import Card, Deck
from passcode import getPasscode, getPasscodeList

# Import test modules
from test_helpers import multiprocess
from test_helpers import taskCheckCards
from test_helpers import taskCheckPasscode

NUM_CORES = 5


# ---------- PART 1: Function for a n-sided die ----------
def test_nsided_die():
    N = 1000
    dieProbArr = [0.20, 0.05, 0.10, 0.25, 0.30, 0.10] 

    # Preallocate an N sized numpy array
    dieOutputArr = np.empty(N, dtype=int)

    # Run nsided_die function N times
    for index in range(N):
        # Populate array with output die number
        dieOutputArr[index] = nsided_die(dieProbArr)

    # Create frequency map, start counting from 1, as dice starts from 1
    frequencies = np.bincount(dieOutputArr, minlength=6)[1:]

    # Plot frequency of the output array
    plot.title("Frequency of Skewed Die")
    plot.xlabel("Dice Number")
    plot.ylabel("Frequency")
    plot.stem(frequencies)
    plot.show()    

    # Plot the PMF of the output array
    plot.title("PMF of Skewed Die")
    plot.xlabel("Dice Number")
    plot.ylabel("Probability")
    plot.stem(dieProbArr)
    plot.show()    


# ---------- PART 2: Number of rolls for two die to sum to 6 or 9 ----------
def test_sum_6_or_9():
    # Create fair dice distribution with list multiplication
    N = 100_000
    dieProbArr = [1/6] * 6

    # Prealllocate an N sized numpy array
    dieOutputArr = np.empty(N, dtype=int)

    # Repeat experiment N times
    for index in range(N):
        rolls  = 0
        dieSum = 0
        while True:
            # Get values of two rolls 
            diceA  = nsided_die(dieProbArr)
            diceB  = nsided_die(dieProbArr)
            dieSum = diceA + diceB
            
            # Terminate loop if sum of 6 or 9 is found
            if dieSum == 6:
                break
            elif dieSum == 9:
                break 

            rolls += 1

        # Append number of attempts required into array
        dieOutputArr[index] = rolls

    # Calculate the frequencies of the roll attempts
    frequencies = np.bincount(dieOutputArr)

    # Get roll array from total rolls
    rollArray = np.linspace(1, len(frequencies), num=len(frequencies), dtype=int)

    # Calculate the probability by referencing total experiments
    sumProbArr = frequencies / N

    #Plot PMF of the output array
    plot.title("PMF of Rolls Required for 6 or 9 Sum")
    plot.xlabel("Rolls Required")
    plot.ylabel("Probability")
    plot.stem(rollArray, sumProbArr)
    plot.show()    


# ---------- PART 3: Getting 500 heads when tossing 1000 coins  ----------
def test_coin_toss():
    HEAD, TAIL   = True, False 
    HEAD_SUCCESS = 500
    NUM_COINS    = 1000
    N            = 100_000
    success      = 0 

    # Toss 1000 fair coins, 100,000 times
    coin_flips = np.random.choice([HEAD, TAIL], size = [N, NUM_COINS])
        
    # Success if EXACTLY 500 heads
    headCounts = np.sum(coin_flips == HEAD, axis = 1)
    success = np.sum(headCounts == HEAD_SUCCESS)

    print(f"Probability of 500 heads in 1000 tosses: {success / N}")


# ---------- PART 4: Getting 4 of a kind from a deck of cards ----------
def test_4_kind():  
    NUM_CARD = 5
    NUM_KIND = 4
    N = 1_000_000
    
    successes = multiprocess(NUM_CORES, N, taskCheckCards, [NUM_CARD, NUM_KIND])
    print(f"Probability of 4 of a kind: {successes / N}")


# ---------- PART 5: The Password Hacking Problem ----------
def test_hack_passcode():
    M_HACKER_LIST = [10 ** 4, 10 ** 5]
    N = 1000

    # Repeat experiment N times for M sizes in hacker list,
    # for M in M_HACKER_LIST:
    #     successes = multiprocess(NUM_CORES, N, taskCheckPasscode, [M])
    #     print(f"Probability of passcode in 10^{int(log10(M))} hacker list: {successes / N}")

    # Repeat experiment until probability is 0.5
    K_p = 5000  
    epsilon = 1e-3 
    M = 1000
    N = 5000
    probability = 0
    while not isclose(probability, 0.5, abs_tol=epsilon):
        successes = multiprocess(NUM_CORES, N, taskCheckPasscode, [int(M)])
        probability = successes / N

        adjustment = (0.5 - probability) * K_p
        M += adjustment
        print(M, probability)

    print(f"M for 0.5 probability: {M}")

    
# Main function is used for desired test cases
def main():
    # test_nsided_die()
    # test_sum_6_or_9()
    # test_coin_toss()
    # test_4_kind()
    test_hack_passcode()


# Call main if run from the command line
if __name__ == "__main__":
    main()