"""
Zach Koverman
5/6/24
ECON 481
Problem Set 5

This file contains functions written as exercises for Problem Set 5 in
ECON 481 - Data Science Computing for Economics
"""
import requests
from bs4 import BeautifulSoup

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_5.py"

def scrape_code(url: str) -> str:
    """
    Exercise 1 - Takes the URL to a slide deck for a lecture from the course 
    website and scrapes all code included on slides in that lecture. Returns a 
    string containing all the scraped code.
    """
    req = requests.get(url, timeout=1)
    if req.ok:
        soup = BeautifulSoup(req.text)
        code = soup.find_all('code', {'class': 'sourceCode python'})

    return code

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    url_l5 = 'https://lukashager.netlify.app/econ-481/05_web_scraping#/'
    print(scrape_code(url_l5))

if __name__ == "__main__":
    main()
