import random as rand

def tx_rx_bit(p0, e0, e1):
    M = rand.random() # Used for message chance 
    T = rand.random() # Used for receive chance

    # Set S
    S = True if M <= p0 else False;

    # Set R
    if   S == False and T <= e0:
        R = True
    elif S == False and T > e0:
        R = False
    elif S == True and T > e1:
        R = True
    elif S == True and T <= e1:
        R = False
    else:
        printf("ERROR: R not computed")

    # Return array for user debugging
    return [S, R]