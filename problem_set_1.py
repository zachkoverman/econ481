"""
Zach Koverman
4/1/24
ECON 481
Problem Set 1

This file contains functions written as exercises for Problem Set 1 in
ECON 481 - Data Science Computing for Economics
"""

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_1.py"

def evens_and_odds(n: int) -> dict:
    """
    Exercise 2 - Takes a natural number n. If n is even, returns the sum of all 
    even natural numbers preceding n. If n is odd, returns the sum of all odd 
    natural numbers preceding n.
    """
    sum_evens = 0
    sum_odds = 0

    for i in range(n):
        if i % 2 == 0:
            sum_evens += i
        else:
            sum_odds += i
    sums_dict = {'evens': sum_evens, 'odds': sum_odds}

    return sums_dict

def main():
    """
    Calls each function to test my solutions to the exercises in this 
    problem set.
    """
    print(evens_and_odds(4))

if __name__ == "__main__":
    main()
 