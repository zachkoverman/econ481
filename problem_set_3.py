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
    is_null = pd.isna(df[col])
    nulls_series = df[col][is_null]
    nulls_length = nulls_series.size

    return nulls_length

def clean_data(emissions_data: pd.DataFrame,
               parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Exercise 4 - 
    """
    merged_df = pd.merge(emissions_data,
                         parent_data,
                         left_on=['year', 'Facility Id'],
                         right_on=['year', 'GHGRP FACILITY ID'],
                         how='left')
    subset_columns = ['Facility Id', 'year', 'State',
                      'Industry Type (sectors)', 
                      'Total reported direct emissions', 'PARENT CO. STATE', 
                      'PARENT CO. PERCENT OWNERSHIP']
    merged_df = merged_df[subset_columns]
    merged_df.columns = [c.lower() for c in merged_df.columns]

    return merged_df

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Exercise 5 - 
    """
    return None

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    yearly_data_df = import_yearly_data([2021, 2022])
    print("Head and descriptive statistics for yearly emissions DataFrame")
    print(yearly_data_df.head(5))
    print(yearly_data_df.describe())

    # Exercise 2
    parent_companies_df = import_parent_companies([2021, 2022])
    print("\nHead and descriptive statistics for parent companies DataFrame")
    print(parent_companies_df.head(5))
    print(parent_companies_df.describe())

    # Exercise 3
    print('\nNumber of null values for Facility ID: ' \
          f'{n_null(parent_companies_df, "GHGRP FACILITY ID")}')
    print('\nNumber of null values for FRS ID: ' \
          f'{n_null(parent_companies_df, "FRS ID (FACILITY)")}')

    # Exercise 4
    print(clean_data(yearly_data_df, parent_companies_df))

    # Exercise 5


if __name__ == "__main__":
    main()
