"""
Zach Koverman
4/10/24
ECON 481
Problem Set 2

This file contains functions written as exercises for Problem Set 2 in
ECON 481 - Data Science Computing for Economics.
"""
import numpy as np
import scipy

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_2.py"

def simulate_data(seed: int=481) -> tuple:
    """
    Exercise 1 - Simulates 1000 observations (y) of a data generating process 
    given by a specific linear equation with three normally distributed 
    variables X and a normally distributed error term epsilon.
    
    Takes an optional seed to set for a random number generator. If
    not specified, seed is set to 481. Returns a tuple of two np.array objects; 
    the first is 1000 x 1 containing y values, and the second is 1000 x 3 
    containing values for x1, x2, and x3 for each observation.
    """
    rng = np.random.default_rng(seed=seed)
    y_arr = np.zeros((1000, 1))
    x_arr = np.zeros((1000, 3))

    x_arr[:, 0] = rng.normal(0, np.sqrt(2), 1000)
    x_arr[:, 1] = rng.normal(0, np.sqrt(2), 1000)
    x_arr[:, 2] = rng.normal(0, np.sqrt(2), 1000)
    epsilon = rng.normal(0, 1, 1000)

    y_arr = 5 + (3 * x_arr[:, 0]) + (2 * x_arr[:, 1]) \
            + (6 * x_arr[:, 2]) + epsilon
    y_arr = np.reshape(y_arr, (1000, 1))

    return y_arr, x_arr

def negative_ll(beta: np.array, y_arr: np.array, x_arr: np.array) -> np.array:
    """
    (Supplementary) - Returns the negative log likelihood for given arrays 
    holding simulated data and a set of coefficients.
    """
    beta = beta.reshape((-1, 1)) # fixes tiny coef problem - need (4,1) not (4,)
    # P(error for each data point) calculated with p.m.f. for N(0, 1)
    indiv_error_prob = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y_arr - x_arr @ beta) ** 2))
    total_error_prob = -1 * np.sum(np.log(indiv_error_prob))
    return total_error_prob

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    Exercise 2 - Estimates MLE coefficients for a given set of observations by 
    finding the coefficients that minimize the negative log likelihood. Returns 
    an array containing the coefficients.
    """
    betas_array = np.ones(4)
    X = np.c_[np.ones(X.shape[0]).reshape(-1, 1), X]

    min_ll_coef = scipy.optimize.minimize(fun=negative_ll, \
                                          args=(y, X), \
                                          x0=betas_array, \
                                          method='Nelder-Mead')

    return min_ll_coef

def sse(beta: np.array, y_arr: np.array, x_arr: np.array) -> np.array:
    """
    (Supplementary) Returns the sum of squared errors for given arrays holding
    simulated data and a set of coefficients.
    """
    beta = beta.reshape((-1, 1)) # fixes tiny coef problem - need (4,1) not (4,)
    return np.sum((y_arr - (x_arr @ beta)) ** 2)

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    Exercise 3 - Estimates OLS coefficients for a given set of observations by 
    finding the coefficients that minimize the sum of squared errors. Returns 
    an array containing the coefficients.
    """
    betas_array = np.ones(4)
    X = np.c_[np.ones(X.shape[0]).reshape(-1, 1), X]

    min_sse_coef = scipy.optimize.minimize(fun=sse, \
                                       args=(y, X), \
                                       x0=betas_array, \
                                       method='Nelder-Mead')

    return min_sse_coef

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    sim_data = simulate_data(323)
    print(f'Shape of simulated y array: {sim_data[0].shape}')
    print(f'Mean of simulate y array: {np.mean(sim_data[0])}')
    print(f'Shape of simulated X array: {sim_data[1].shape}')
    print(f'Mean of simulate X array: {np.mean(sim_data[1])}')

    # Exercise 2
    ex_2_coef_array = estimate_mle(sim_data[0], sim_data[1]).x
    print(f'Coefficients estimated with MLE: {ex_2_coef_array}')

    # Exercise 3
    ex_3_coef_array = estimate_ols(sim_data[0], sim_data[1]).x
    print(f'Coefficients estimated with OLS: {ex_3_coef_array}')

if __name__ == "__main__":
    main()
