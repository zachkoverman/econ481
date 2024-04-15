"""
Zach Koverman
4/17/24
ECON 481
Problem Set 3

This file contains functions written as exercises for Problem Set 3 in
ECON 481 - Data Science Computing for Economics.
"""

import pandas as pd

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_3.py"

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Exercise 1 - 
    """
    df_list = []
    for target_year in years:
        year_df = pd.read_excel("https://lukashager.netlify.app/econ-481/data" \
                                f"/ghgp_data_{target_year}.xlsx",
                                header=3)
        year_df['year'] = target_year
        df_list.append(year_df)
    annual_emissions = pd.concat(df_list)

    return annual_emissions

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Exercise 2 - 
    """
    df_list = []
    for target_year in years:
        year_df = pd.read_excel("https://lukashager.netlify.app/econ-481/data" \
                                "/ghgp_data_parent_company_09_2023.xlsb",
                                sheet_name=str(target_year))
        year_df.dropna(axis=0, how='all')
        year_df['year'] = target_year
        df_list.append(year_df)
    company_emissions = pd.concat(df_list)

    return company_emissions

def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Exercise 3 - 
    """


    return None

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    print(import_yearly_data([2021, 2022]).head(5))
    print(import_yearly_data([2021, 2022]).describe())

    # Exercise 2
    print(import_parent_companies([2021, 2022]).head(5))
    print(import_parent_companies([2021, 2022]).describe())

if __name__ == "__main__":
    main()
