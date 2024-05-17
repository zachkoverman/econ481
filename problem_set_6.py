"""
Zach Koverman
5/15/24
ECON 481
Problem Set 6

This file contains functions written as exercises for Problem Set 6 in
ECON 481 - Data Science Computing for Economics
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def github() -> str:
    """
    Exercise 0 - Returns the URL to this file in my GitHub repository for this
    class.
    """
    return "https://github.com/zachkoverman/econ481/blob/main/problem_set_6.py"


def std() -> str:
    """
    Exercise 1 -
    """
    query = """
    WITH s AS (
        SELECT itemId, AVG(bidAmount) OVER (PARTITION BY itemId) AS bidAvg
        FROM bids
    )
    SELECT b.itemId AS itemId,
        SQRT((SUM(POW(b.bidAmount - s.bidAvg, 2))) / (COUNT(b.bidAmount)) - 1) AS std
    FROM bids AS b LEFT JOIN s ON b.itemId = s.itemId
    GROUP BY b.itemId
    HAVING COUNT(b.itemId) > 1 AND std IS NOT NULL
    """

    return query


def bidder_spend_frac() -> str:
    """
    Exercise 2 - 
    """
    query = """
    WITH s AS (
        SELECT itemId,
            bidderName,
            MAX(bidAmount) AS highBid,
            (CASE WHEN 
                MAX(bidAmount) OVER (PARTITION BY itemId) = bidAmount 
                THEN MAX(bidamount) 
                ELSE 0 END) AS spent
        FROM bids
        GROUP BY itemId, bidderName
    )
    SELECT bidderName,
        SUM(spent) AS total_spend,
        SUM(highBid) AS total_bids,
        (SUM(spent) / SUM(highBid)) AS spend_frac
    FROM s
    GROUP BY bidderName
    """

    return query


def min_increment_freq() -> str:
    """
    Exercise 3 - 
    """
    query = """
    WITH s AS (
        SELECT (
            CASE WHEN (bidAmount - LAG(b.bidAmount) 
                       OVER (PARTITION BY b.itemId
                             ORDER BY b.bidTime)) = i.bidIncrement
            THEN 1.0
            ELSE 0.0
            END) AS isMinBid
        FROM bids AS b 
            INNER JOIN items AS i ON b.itemId = i.itemId
        WHERE isBuyNowUsed = 0)
    SELECT SUM(isMinBid) / COUNT(isMinBid) AS freq
    FROM s
    """

    return query


def win_perc_by_timestamp() -> str:
    """
    Exercise 4 -
    """
    query = """
    WITH t AS (
        SELECT itemId,
               startTime,
               endTime,
               julianday(endTime) - julianday(startTime) AS length
          FROM items)
    SELECT (CAST(1 + ((julianday(t.endTime) - julianday(s.bidTime)) / t.length) * 10 
                AS INTEGER)) AS timestamp_bin,
           SUM(isWinningBid) / COUNT(isWinningBid) AS win_perc
      FROM (SELECT itemId,
                   bidTime,
                   (CASE WHEN MAX(bidAmount) 
                              OVER (PARTITION BY itemId) = bidAmount
                         THEN 1.0
                         ELSE 0.0
                         END) AS isWinningBid
              FROM bids) AS s
           INNER JOIN t ON t.itemId = s.itemId
     GROUP BY timestamp_bin
    """

    return query


class DataBase:
    """
    This class allows users to create a database from a .db file and pass 
    strings to query it. 
    """

    def __init__(self, loc: str, db_type: str = 'sqlite') -> None:
        """
        Initializes the class and creates a connection to the database.
        """
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')

    def query(self, q: str) -> pd.DataFrame:
        """
        Takes a string containing a SQL query, queries the database, and 
        returns a DataFrame containing the output of the query.
        """
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return df


def main():
    """
    Calls functions to demonstrate my solutions to the exercises in this 
    problem set.
    """
    # Setting up Database object
    path = '/Users/zachkoverman/Desktop/School/Senior Year/ECON 481 - Data '\
           'Science Computing for Economics/datasets/auctions.db'
    auctions = DataBase(path)

    # Calling functions to query auctions database
    # Exploration
    q_bids = "SELECT * FROM bids LIMIT 5"
    print(auctions.query(q_bids).columns)
    print(auctions.query(q_bids))
    q_items = "SELECT * FROM items LIMIT 5"
    print(auctions.query(q_items).columns)
    q_items_2 = "SELECT bidIncrement, isBuyNowUsed, itemId FROM items LIMIT 5"
    print(auctions.query(q_items_2))

    # Exercise 1
    q_e1 = std()
    query_df_e1 = auctions.query(q_e1)
    print(f'Exercise 1:\n{query_df_e1.head(15)}')
    print(f'Number of rows: {len(query_df_e1)}\n')

    # Exercise 2
    q_e2 = bidder_spend_frac()
    query_df_e2 = auctions.query(q_e2)
    print(f'Exercise 2:\n{query_df_e2.head(15)}')
    print(f'Number of rows: {len(query_df_e2)}\n')

    # Exercise 3
    q_e3 = min_increment_freq()
    query_df_e3 = auctions.query(q_e3)
    print(f'Exercise 3:\n{query_df_e3.head(40)}')
    print(f'Number of rows: {len(query_df_e3)}\n')

    # Exercise 4
    q_e4 = win_perc_by_timestamp()
    query_df_e4 = auctions.query(q_e4)
    print(f'Exercise 4:\n{query_df_e4.head(15)}')
    print(f'Number of rows: {len(query_df_e4)}\n')


if __name__ == '__main__':
    main()
