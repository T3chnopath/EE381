import random as rand
from typing import List

PASSCODE_LEN = 4
def getPasscode() -> str:
    """
    This function takes an n length array of die side probabilities, and rolls it.

    Parameters:
    - None

    Returns:
        str: The random 4 digit passcode
    """

    # Generate the passcode
    passcode = ""
    passcode_digits = rand.choices('0123456789', k=PASSCODE_LEN)
    passcode = ''.join(passcode_digits)

    return passcode

def getPasscodeList(size: int) -> List[str]:
    """
    Generates a randomized hacker passcode list.

    Parameters:
    - size (int): The size of the randomized passcode list

    Returns:
        List[str]: The list of passcodes of specified size
    """

    return [getPasscode() for _ in range(size)]