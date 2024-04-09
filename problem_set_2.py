"""
Zach Koverman
4/10/24
ECON 481
Problem Set 2

This file contains functions written as exercises for Problem Set 2 in
ECON 481 - Data Science Computing for Economics.
"""
import numpy as np

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_2.py"

def simulate_data(seed: int=481) -> tuple:
    """
    Exercise 1 -
    """
    rng = np.random.default_rng(seed=seed)
    y_arr = np.ones((1000, 1))
    x_arr = np.ones((1000, 3))
    
    for i in range(1000):
        x_arr[i, 0] = rng.normal(0, 2)
        x_arr[i, 1] = rng.normal(0, 2)
        x_arr[i, 2] = rng.normal(0, 2)
        ep_i = rng.normal(0, 1)
        y_arr[i] = 5 + (3 * x_arr[i, 0]) + (2 * x_arr[i, 1]) \
                   + (6 * x_arr[i, 2]) + ep_i

    return y_arr, x_arr

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    print(simulate_data(55))

if __name__ == "__main__":
    main()
