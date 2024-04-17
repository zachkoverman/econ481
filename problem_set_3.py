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
    Exercise 1 - Reads Excel files containing emissions data from year(s) 
    specified in a given list. Returns one DataFrame object concatenating the
    data together, with the corresponding year added as a new column.
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
    Exercise 2 - Reads an Excel file containing information on polluting 
    comapnies. Sheets are selected according to years passed in a list and 
    concatenated together. Drops any rows where all values are null. Returns 
    one DataFrame object with the concatenated data and the corresponding year 
    added as a new column.
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
    Exercise 3 - Takes a DataFrame and column name and returns the number of
    null values in the specified column.
    """
    is_null = pd.isna(df[col])
    nulls_series = df[col][is_null]
    nulls_length = nulls_series.size

    return nulls_length

def clean_data(emissions_data: pd.DataFrame,
               parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Exercise 4 - Takes two DataFrames, joins them, then subsets to a handful of
    columns and converts the names to lowercase. Returns the processed 
    DataFrame.
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
    Exercise 5 - Groups a given DataFrame by given variables, aggregating to 
    calculate the mininmum, median, mean, and maximum values for direct 
    emissions and parent co. ownership. Returns the grouped data in descending
    order of mean direct emissions.
    """
    grouped_df = df.groupby(group_vars)[['total reported direct emissions', \
                                         'parent co. percent ownership']]\
                   .agg(['min', 'median', 'mean', 'max'])\
                   .sort_values(by=('total reported direct emissions', \
                                    'mean'), \
                                ascending=False)

    return grouped_df

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    print('==============\n  Exercise 1\n==============\n')
    yearly_data_df = import_yearly_data([2021, 2022])
    print("Head and descriptive statistics for yearly emissions DataFrame:")
    print(f'\n{yearly_data_df.head(5)}')
    print(f'\n{yearly_data_df.describe()}')

    # Exercise 2
    print('\n==============\n  Exercise 2\n==============\n')
    parent_companies_df = import_parent_companies([2021, 2022])
    print("Head and descriptive statistics for parent companies DataFrame:")
    print(f'\n{parent_companies_df.head(5)}')
    print(f'\n{parent_companies_df.describe()}')

    # Exercise 3
    print('\n==============\n  Exercise 3\n==============\n')
    print('Number of null values for Facility ID: ' \
          f'{n_null(parent_companies_df, "GHGRP FACILITY ID")}')
    print('\nNumber of null values for FRS ID: ' \
          f'{n_null(parent_companies_df, "FRS ID (FACILITY)")}')

    # Exercise 4
    print('\n==============\n  Exercise 4\n==============\n')
    cleaned_data = clean_data(yearly_data_df, parent_companies_df)
    print(f'First 5 rows of cleaned data:\n{cleaned_data.head(5)}')

    # Exercise 5
    print('\n==============\n  Exercise 5\n==============\n')
    agg_data = aggregate_emissions(cleaned_data, ['state'])
    print(f'Emissions aggregations (ordered by mean emissions):\n{agg_data}')

    # Optional Bonus
    print('\n==============\nOptional Bonus\n==============\n')
    agg_data = aggregate_emissions(cleaned_data, ['state'])
    data_median = agg_data.sort_values(by=('total reported direct emissions',
                                           'median'), 
                                       ascending=False)
    print('Emissions aggregations (ordered by median emissions):'\
          f'\n{data_median}')

if __name__ == "__main__":
    main()
