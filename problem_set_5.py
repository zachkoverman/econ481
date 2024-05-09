"""
Zach Koverman
5/8/24
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
    website and scrapes all python code included on slides in that lecture. 
    Returns a string containing all the scraped code.
    """
    req = requests.get(url, timeout=1)

    # Getting each line of code as an element in a list.
    if req.ok:
        soup = BeautifulSoup(req.text, features = "html.parser")
        code = soup.find_all('code', {'class': 'sourceCode python'})
        lines = [line.text for line in code]

    # Cleaning collected strings, allowing removal of lines starting with '%'
    lines_no_pct = []
    for python_line in lines:
        delim = '\n'
        split_line_list = python_line.split(delim)
        for split_line in split_line_list:
            if len(split_line) == 0:
                lines_no_pct.append('')
            elif split_line[0] != '%':
                lines_no_pct.append(split_line)

    single_string = '\n'.join(lines_no_pct)

    return single_string

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    url_l1 = 'https://lukashager.netlify.app/econ-481/01_intro_to_python#/'
    url_l2 = 'https://lukashager.netlify.app/econ-481/'\
             '02_numerical_computing_in_python#/'
    url_l5 = 'https://lukashager.netlify.app/econ-481/05_web_scraping#/'
    print(scrape_code(url_l2))

if __name__ == "__main__":
    main()
