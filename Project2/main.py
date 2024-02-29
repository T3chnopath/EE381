# Imporrt user libraries
from tx_rx_bit import tx_rx_bit

# Constants
P0 = 0.35 # Probability of 0
E0 = 0.01 # Probability of 0 misread
E1 = 0.02 # Probability of 1 misread


# ---------- PART 1: Probability of Erroneous Transmission ----------
def testErrTransmit():
    N = 100_000_000
    failure = 0 # Number of times S != R
    
    for i in range(N):
        S, R = tx_rx_bit(P0, E0, E1)
       
        if S != R:
            failure += 1
    
    print(f"Probability of tx / rx failure: {failure / N:.5f}")


# ---------- PART 2: Conditional Probability - P( R=1 | S=1 ) ----------
def testR1GivenS1():
    N = 100_000_000
    totalS = 0 
    success = 0 # Number of times R == S

    # Repeat experiment N times
    for i in range(N):
        S, R = tx_rx_bit(P0, E0, E1)
       
        # For P(S) 
        if S:
            totalS += 1

            # For P(R ∩ S) 
            if R:
                success += 1
    
    # P(R = 1 | S = 1) = P(R ∩ S) / P(S)
    print(f"Probability of R = 1 | S = 1: {(success / totalS):.5f}")


# ---------- PART 3: Conditional Probability - P( S=1 | R=1 ) ----------
def testS1GivenR1():
    N = 100_000_000
    totalR = 0
    success = 0 # Number of times S == R

    # Repeat experiment N times
    for i in range(N):
        S, R = tx_rx_bit(P0, E0, E1)
       
        # For P(R) 
        if R:
            totalR += 1

            # For P(S ∩ R) 
            if S:
                success += 1

    # P(S = 1 | R = 1) = P(S ∩ R) / P(R)
    print(f"Probability of S = 1 | R = 1: {(success / totalR):.5f}")


# ---------- PART 4: Enhanced Transmission Method (TMR) ----------
def testEnhanceTransmit():
    N = 100_000_000
    failure = 0 # Number of times S != R

    # Repeat experiment N times
    for i in range(N):
        S, R = tx_rx_bit(P0, E0, E1, True)

        # Count failure when TX and RX bits are different
        if S != R: 
            failure += 1

    print(f"Probability to decode incorrectly with TMR: {(failure / N):.3f}")


# Main function is used for desired test cases
def main():
    testErrTransmit()
    testR1GivenS1()
    testS1GivenR1()
    testEnhanceTransmit()

# Call main if run from the command line
if __name__ == "__main__":
    main()