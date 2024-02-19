# Python STD Library Helpers
from multiprocessing import Pool

# Import user modules
from cards import Deck
from passcode import getPasscode, getPasscodeList

# Multiprocess helper
def multiprocess(numProc, totalRuns, task, taskArgs=None):
    # Create tuple of arguments for star map
    args = [(totalRuns // numProc)]

    # Append arguments 
    for arg in taskArgs:
        args.append(arg)

    # Spin up task on the specified cores
    with Pool(numProc) as pool:
        results = pool.starmap(task, (tuple(args) for i in range(numProc)))

    # Return list for external filtering
    return results

# Helper to find median of an array
def median(array):
    # First, sort the array
    sorted_array = sorted(array)
    
    # Find the number of elements in the array
    n = len(sorted_array)
    
    # Check if the number of elements is odd
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_array[n // 2]
    else:
        # If even, return the average of the two middle elements
        return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

# Card helpers
def taskCheckCards(N, numCards, numKind):
    successes = 0
    for x in range(N):
        # Empty deck 
        deck = Deck()

        # Create a hand of 5 cards
        hand = [deck.drawCard() for card in range(numCards)]

        # Get the ranks in the hand
        ranks = [card.getRank() for card in hand]

        # See if there are 4 identical cards
        for rank in ranks:
            if ranks.count(rank) >= numKind:
                successes += 1
                break

    return successes

# Passcode helpers
def taskCheckPasscode(N, hackerListSize):
    success = 0 
    for x in range(N):
        if getPasscode() in getPasscodeList(hackerListSize):
            success += 1
    
    return success