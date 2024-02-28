import random as rand

def tx_rx_bit(p0, e0, e1, enhanced = False):
    R_buff = [] 
    M = rand.random() # Used for message chance 
    
    # Set S
    S = True if M <= p0 else False;

    # If enhanced transmission, repeat send    
    if enhanced:
        txCount = 3
    else:
        txCount = 1

    for i in range(txCount):
        T = rand.random() # Used for receive chance
        # Set R array
        if   S == False and T <= e0:
            R_buff.append(True)
        elif S == False and T > e0:
            R_buff.append(False)
        elif S == True and T > e1:
            R_buff.append(True)
        elif S == True and T <= e1:
            R_buff.append(False)
        else:
            print("ERROR: R not computed")

    # If enhanced, perform majority vote
    if enhanced:
        return[S, bool(sum(R_buff) > len(R_buff) / 2)]
    # Otherwise, return first element 
    else:
        return [S, R_buff[0]]