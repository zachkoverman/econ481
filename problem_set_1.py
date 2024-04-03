"""
Zach Koverman
4/1/24
ECON 481
Problem Set 1

This file contains functions written as exercises for Problem Set 1 in
ECON 481 - Data Science Computing for Economics
"""
from typing import Union
from datetime import datetime

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

    return {'evens': sum_evens, 'odds': sum_odds}

def time_diff(date_1: str, date_2: str, out: str="float") -> Union[str,float]:
    """
    Exercise 3 - Takes two strings representing dates in the format 
    "YYYY-MM-DD". Argument "out" specifies how to format the return: when 
    "float", it returns the number of days between the two dates. If "string",
    it returns a string containing a sentence telling the difference in days.
    """
    dt_1 = datetime.strptime(date_1, "%Y-%m-%d")
    dt_2 = datetime.strptime(date_2, "%Y-%m-%d")
    delta = dt_1 - dt_2

    if out == "string":
        return f"There are {abs(delta.days)} days between the two dates."
    else:
        return abs(delta.days)

def reverse(in_list: list) -> list:
    """
    Exercise 4 - Takes a list and returns the same elements in reversed order.
    """
    out_list = []
    for i in range(1, len(in_list) + 1):
        out_list.append(in_list[-i])

    return out_list

def prob_k_heads(n: int, k: int) -> float:
    """
    Exercise 5 - Takes integers k and n, assuming n is larger than k, 
    and returns the probability of seeing k successes in n tries of flipping a 
    coin. This is calculated using the binomial probability mass function.
    """
    # prob = (n choose k) * (success prob)^k * (fail prob)^n-k
    # Calculating binomial coefficient
    n_fact = 1
    k_fact = 1
    diff_fact = 1
    for i in range(1, n+1):
        n_fact *= i
    for i in range(1, k+1):
        k_fact *= i
    for i in range(1, (n-k)+1):
        diff_fact *= i
    n_choose_k = n_fact / (k_fact * diff_fact)

    # Calculating the probability of any one permutation each flip
    prob_successes = (1/2) ** k
    prob_failures = (1/2) ** (n - k)

    return n_choose_k * prob_successes * prob_failures

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 2
    print(evens_and_odds(4))
    print(evens_and_odds(9))

    # Exercise 3
    print(time_diff("2024-04-02", "2001-12-20"))
    print(time_diff("2001-12-20", "2024-04-02", "string"))
    print(time_diff("2024-04-01", "2024-04-02", "string"))

    # Exercise 4
    print(reverse(['a', 'b', 'c']))
    print(reverse([]))
    print(reverse(['a']))
    print(reverse(['a', 'b', 'c', 'd', 'e', 'f']))

    # Exercise 5
    print(prob_k_heads(1, 1))
    print(prob_k_heads(10, 3))

if __name__ == "__main__":
    main()
