"""
Zach Koverman
4/22/24
ECON 481
Problem Set 4

This file contains functions written as exercises for Problem Set 4 in
ECON 481 - Data Science Computing for Economics
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_4.py"

def load_data() -> pd.DataFrame:
    """
    Exercise 1 - Loads Tesla stock price history and returns it as a DataFrame.
    """
    tesla_data = pd.read_csv('https://lukashager.netlify.app/econ-481/'\
                             'data/TSLA.csv',
                             index_col=0,
                             parse_dates=True)
    return tesla_data

def plot_close(df: pd.DataFrame,
               start: str='2010-06-29',
               end: str='2024-04-15') -> None:
    """
    Exercise 2 - Takes a DataFrame of Tesla stock price data and plots the 
    closing price each day. Start and end dates can be specified, but if not, 
    defaults to the period June 29 2010 through April 15 2024.
    """
    # Filtering data to selected data range
    is_date_range = (df.index >= start) & (df.index <= end)
    df = df[is_date_range]

    # Plotting figure and adjusting details
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(df['Close'], color='navy')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (in $)')
    ax.set_title(f'Daily Closing Price of TSLA, {start} through {end}')

    # Adjusting ticks on x axis to be readable (not include all points)
    date_locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(date_locator)
    date_formatter = mdates.ConciseDateFormatter(date_locator)
    ax.xaxis.set_major_formatter(date_formatter)

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    tsla_df = load_data()
    print(tsla_df.head(5))

    # Exercise 2
    plot_close(tsla_df)
    plot_close(tsla_df, '2020-01-01', '2020-12-31')


if __name__ == "__main__":
    main()

# %%
