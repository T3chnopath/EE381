import numpy as np
import matplotlib.pyplot as plt
from   scipy.stats import gamma
from   scipy.stats import norm

def plotDist(dist_type: str, a: float, b: float, N: int, n: int) -> None:
    """
    Simulates and plots distributions for uniform or exponential random variables.
    
    Parameters:
    - dist_type (str): Type of distribution ('uniform' or 'exponential').
    - a (float): Lower bound for uniform, lambda (rate) for exponential.
    - b (float): Upper bound for uniform. Unused for exponential.
    - N (int): Number of experiments.
    - n (int): Number of random variables to sum.
    """
    
    # Initialize the array to store sums
    X = np.zeros(N)
    
    # Perform simulations
    for k in range(N):
        if dist_type == 'uniform':
            x = (b - a) * np.random.rand(n) + a
        elif dist_type == 'exponential':
            x = np.random.exponential(1/a, n)
        else:
            raise ValueError("Unsupported distribution type")
        
        X[k] = np.sum(x)
    
    # Compute statistics for the summed variables
    if dist_type == 'uniform':
        mu = n * (a + b) / 2
        sig = np.sqrt(n * ((b - a)**2 / 12))
    elif dist_type == 'exponential':
        mu = n / a
        sig = np.sqrt(n) / a
    
    # Plotting PDF
    nbins = 15
    del_x = (max(X) - min(X)) / (nbins - 1)
    bins = np.arange(min(X), max(X) + del_x, del_x)
    h, xout = np.histogram(X, bins=bins, density=True)
    
    plt.figure(1)
    plt.bar(xout[:-1], h, width=del_x, align='edge', alpha=0.6)
    plt.grid(True)
    
    # Overlay plot of theoretical distribution
    z = np.linspace(min(X), max(X), 300)
    if dist_type == 'uniform':
        gf = (1 / (sig * np.sqrt(2 * np.pi))) * np.exp(-(z - mu)**2 / (2 * sig**2))
        plt.plot(z, gf, 'r', linewidth=3)
    elif dist_type == 'exponential':
        rate = a  # Rate is 'a' since lambda = 1/a
        gf = gamma.pdf(z, a=n, scale=1/rate)  # Gamma distribution for sum of exponentials
        plt.plot(z, gf, 'r', linewidth=3)
    
    plt.show()

def plotCartonLifetime(beta, N, num_batteries):
    """
    Simulates the lifetimes of battery cartons and plots the PDF and CDF.

    Parameters:
    - beta (float): The parameter beta (mean = beta, std dev = beta) for the exponential distribution.
    - N (int): Number of cartons to simulate.
    - num_batteries (int): Number of batteries per carton.
    """
    # Simulate carton lifetimes
    carton_lifetimes = [np.sum(np.random.exponential(beta, num_batteries)) for _ in range(N)]
    
    # Compute mean and std dev for the normal approximation
    mu = num_batteries * beta
    sigma = np.sqrt(num_batteries) * beta

    # Plotting the PDF
    plt.figure(figsize=(12, 6))
    plt.hist(carton_lifetimes, bins=50, density=True, alpha=0.6, color='b', label='Experimental PDF')
    
    # Normal distribution overlay
    x = np.linspace(min(carton_lifetimes), max(carton_lifetimes), 300)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r-', lw=2, label='Normal Approximation')
    plt.title('PDF of Carton Lifetimes')
    plt.xlabel('Lifetime')
    plt.ylabel('Frequency')
    plt.legend()

    # Plotting the CDF
    plt.figure(figsize=(12, 6))
    plt.hist(carton_lifetimes, bins=50, density=True, cumulative=True, alpha=0.6, color='b', label='Experimental CDF')
    plt.plot(x, norm.cdf(x, mu, sigma), 'r-', lw=2, label='Normal Approximation CDF')
    plt.title('CDF of Carton Lifetimes')
    plt.xlabel('Lifetime')
    plt.ylabel('Cumulative Probability')
    plt.legend()
    
    plt.show()


# ---------- PART 1: The Centrl Limit Theorem ----------
def testCentralLimitTheorem():
    plotDist('uniform', 2, 4.5, 10000, 1)   # n = 1
    plotDist('uniform', 2, 4.5, 10000, 2)   # n = 2
    plotDist('uniform', 2, 4.5, 10000, 5)   # n = 5
    plotDist('uniform', 2, 4.5, 10000, 10)  # n = 10
    plotDist('uniform', 2, 4.5, 10000, 15)  # n = 15

# ---------- PART 2: Exponential Distributed Random Variables ----------
def testExponentialDist():
    plotDist('exponential', 2, None, 10000, 1)   # n = 1
    plotDist('exponential', 2, None, 10000, 2)   # n = 2
    plotDist('exponential', 2, None, 10000, 5)   # n = 5
    plotDist('exponential', 2, None, 10000, 10)  # n = 10
    plotDist('exponential', 2, None, 10000, 15)  # n = 15

# ---------- PART 3: Distribution of the Sum of RVs ----------
def testCartonLifeTime():
    plotCartonLifetime(40, 10000, 24)


def main():
    testCentralLimitTheorem() 
    testExponentialDist()
    testCartonLifeTime()

# Call main if run from the command line
if __name__ == "__main__":
    main()
