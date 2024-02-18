# Python STD Library Helpers
from multiprocessing import Pool

# Import user modules
from nsided_die import nsided_die
from cards import Card, Deck
from passcode import getPasscode, getPasscodeList

# Multiprocess helper
def multiprocess(numCores, totalRuns, task, taskArgs=None):
    # Create tuple of arguments for star map
    args = [(totalRuns // numCores)]

    # Append arguments 
    for arg in taskArgs:
        args.append(arg)

    # Spin up task on the specified cores
    with Pool(numCores) as pool:
        results = pool.starmap(task, (tuple(args) for i in range(numCores)))

    return sum(results)

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