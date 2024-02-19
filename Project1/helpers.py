# Python STD Library Helpers
from multiprocessing import Pool
from typing import Callable, List, Any

# Import user modules
from cards import Deck
from passcode import getPasscode, getPasscodeList

def multiprocess(numProc: int, totalRuns: int , task: Callable, taskArgs: List[Any]=None):
    """
    Helper function that multiprocesses tasks.

    Parameters:
    - numProc   (int): Number of processes to spin up
    - totalRuns (int): Number of runs of each task, to be split among processes
    - task (Callable): The function to be executed {totalRuns} times in parallel
    - taskArgs (List)[OPTIONAL]: The parameters of the function

    Returns:
        Any: Result of the task
    """

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


def median(array: List[Any]) -> Any:
    """
    Helper function that returns median of an array. Array is assumed to be unsorted.

    Parameters:
        array (List[Any]): Array to find median of

    Returns:
        Any: Median of the input array
    """

    # Sort the array
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


def taskCheckCards(N: int, numCards: int, numKind: int) -> int:
    """
    Task helper function for testing the cards module. Randomly draws cards and sees if there are identical kinds.

    Parameters:
        N        (int): Number of times to repeat experiment
        numCards (int): How many cards to draw
        numKind  (int): How many identical kinds

    Returns:
        int: Number of times {numKind} kinds are found successfuly in N experiments
    """

    successes = 0
    for x in range(N):
        # Empty deck 
        deck = Deck()

        # Create a hand of num cards
        hand = [deck.drawCard() for card in range(numCards)]

        # Get the ranks in the hand
        ranks = [card.getRank() for card in hand]

        # See if there are identical cards of specified kind
        for rank in ranks:
            if ranks.count(rank) >= numKind:
                successes += 1
                break

    return successes


def taskCheckPasscode(N: int, hackerListSize: int) -> int:
    """
    Task helper function for testing the passocde module. 

    Parameters:
        N              (int): Number of times to repeat the experiment
        hackerListSize (int): Size of the hacker list under test

    Returns:
        int: Number of times the passcode is found in the hacker list
    """

    # Check if passcode is in the randomized hacker list
    success = 0 
    for x in range(N):
        if getPasscode() in getPasscodeList(hackerListSize):
            success += 2
    
    return success