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
import statsmodels.formula.api as smf

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

    return

def autoregress(df: pd.DataFrame) -> float:
    """
    Exercise 3 - 
    """
    df['Lag_Close'] = df['Close'].shift(periods=1, freq='D')
    df['Diff'] = df['Close'] - df['Lag_Close']
    df['Lag_Diff'] = df['Diff'].shift(periods=1, freq='D')

    ols_model = smf.ols('Diff ~ Lag_Diff -1', data=df, missing='drop')
    ols_results = ols_model.fit(cov_type='HC1')
    t_stat_beta_0 = ols_results.tvalues

    return t_stat_beta_0

def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Exercise 4 - 


    # Left hand side needs to be indicator variable whether diff is > 0 or not - create new column
    # regress (indicator) ~ lag diff
    """
    df['Diff_Positive'] = df['Diff'] > 0
    df['Diff_Positive'] = df['Diff_Positive'].astype(int)
    df['Lag_Close'] = df['Close'].shift(periods=1, freq="D")

    logit_results = smf.logit('Diff_Positive ~ Lag_Diff -1',
                              data=df,
                              missing='drop').fit()
    t_stat_beta_0 = logit_results.tvalues

    return t_stat_beta_0

def plot_delta(df: pd.DataFrame) -> None:
    """
    Exercise 5 - 
    """
    # Plotting figure and adjusting details
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(df['Diff'], color='darkgreen')
    ax.set_xlabel('Date')
    ax.set_ylabel('Change in Closing Price from Previous Day (in $)')
    ax.set_title('Daily Change in Closing Price of TSLA')

    # Adjusting ticks on x axis to be readable (not include all points)
    date_locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(date_locator)
    date_formatter = mdates.ConciseDateFormatter(date_locator)
    ax.xaxis.set_major_formatter(date_formatter)

    return

def main():
    """
    Calls each function to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Exercise 1
    tsla_df = load_data()
    print(f'Head of TSLA Stock Price Dataset:\n{tsla_df.head(5)}\n')

    # Exercise 2
    plot_close(tsla_df)
    plot_close(tsla_df, '2020-01-01', '2020-12-31')

    # Exercise 3
    print(f'OLS - t Statistic for Beta_0 Hat:\n{autoregress(tsla_df)}\n')

    # Exercise 4
    print(f'Logit - t Statistic for Beta_0 Hat:\n{autoregress_logit(tsla_df)}\n')

    # Exercise 5
    plot_delta(tsla_df)

if __name__ == "__main__":
    main()

# %%
