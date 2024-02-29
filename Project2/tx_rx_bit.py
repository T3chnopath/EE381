import random as rand
from typing import List

def tx_rx_bit(p0: float, e0: float, e1: float, enhanced:bool = False) -> List:
    """
    This function simulates sending (TX) and receiving (RX) a bit. 
    The chances of incorrect transmission and reception are 
    controlled by the 3 arguments.

    Parameters:
        - po (float): Controls probabiltiy of TX bit being 0 or 1
        - e0 (float): "Error 0", chance of 0 received as 1
        = e1 (float): "Error 1", chance of 1 received as 0 
    """

    R_buff = [] 
    M = rand.random() # Generate M for TX bit once
    
    # Set S
    S = True if M <= p0 else False;

    # If enhanced transmission, repeat send {txCount}  times
    if enhanced:
        txCount = 3
    else:
        txCount = 1

    # Iterate over specified txCount size
    for i in range(txCount):
        # Generate T for RX bit every loop
        T = rand.random() 
        
        # Set R array
        if   S == False and T <= e0:
            R_buff.append(True)
        elif S == False and T > e0:
            R_buff.append(False)
        elif S == True and T > e1:
            R_buff.append(True)
        elif S == True and T <= e1:
            R_buff.append(False)

    # If enhanced, perform majority vote
    if enhanced:
        return[S, bool(sum(R_buff) > len(R_buff) / 2)]

    # Otherwise, return first element 
    else:
        return [S, R_buff[0]]