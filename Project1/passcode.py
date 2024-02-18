import random as rand
from typing import List

PASSCODE_LEN = 4
def getPasscode():
    passcode = ""
    
    for x in range(PASSCODE_LEN):
        passcode += str(rand.randint(0, 9))

    return passcode

def getPasscodeList(size: int):
    passcodes = []
    for x in range(size):
        passcodes.append(getPasscode())
    
    return sorted(passcodes)