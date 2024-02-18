import random as rand
from typing import List

PASSCODE_LEN = 4
def getPasscode():
    passcode = ""
    passcode_digits = rand.choices('0123456789', k=PASSCODE_LEN)
    passcode = ''.join(passcode_digits)
    return passcode

def getPasscodeList(size: int):
    return [getPasscode() for _ in range(size)]