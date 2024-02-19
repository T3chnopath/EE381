import random as rand
from typing import List

def nsided_die(probArray: List[float]) -> int:
    """
    This function takes an n length array of die side probabilities, and rolls it.

    Parameters:
    - probArray (List[float]): An array representing the probability of each side

    Returns:
        int: The number resulting from the rol
    """
    
    # Generate random number within probability range
    randomNumber = rand.random()
    
    # Calculate cumulative sum for a distribution of the die probabilities
    distribution = 0
    for index, probability in enumerate(probArray):
        distribution += probability

        # When the random number is found in the distribution, return
        if distribution > randomNumber:
            return index + 1