from typing import (
    List,
    Tuple,
)

import pandas as pd


class Transformer:

    def __init__(self):
        self

    def read_orders(self) -> pd.DataFrame:
        orders = pd.read_csv('orders.csv', header=0, dtype={"orderId": str, "amount" : int, "customer": str, "date": str})
        return orders

    def enrich_orders(self, orders: pd.DataFrame, col_name: str, value: List[str]) -> pd.DataFrame:
        """
        Adds a column to the data frame

        Args:
            orders (pd.Dataframe): The dataframe to be enriched
            col_name (str): Name of the new enriched column
            value (List[str]): Data to go into the new column

        Returns:
            The enriched dataframe
        """
        orders.insert(len(orders.columns) - 1 , col_name , value)
        return orders

    def split_customers(self, orders: pd.DataFrame, threshold: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Splits customers into two groups based on a threshold

        Args:
            orders (pd.DataFrame): The dataframe to be split
            threshold (int): Value to split the customer base on

        Returns:
            Tuple containing the split dataframes
        """
        return (orders[orders['amount'] >= threshold], orders[orders['amount'] < threshold])

# - BONUS TASKS: Which customer placed the highest order amount?
    def max_customer(self, df: pd.DataFrame) -> str:
        max = 0
        customer = ""
        for index, row in df.iterrows:
            if(row['amount'] > max):
                max = row['amount']
                customer = row['customer']
        return customer
# - Which customer placed the lowest order amount?
    def min_customer(self, df: pd.DataFrame) -> str:
        min = float('inf')
        customer = ""
        for index, row in df.iterrows:
            if(row['amount'] < min):
                min = row['amount']
                customer = row['customer']
        return customer

# - What was the average order amount across all customers?
    def average_order(self, df: pd.DataFrame) -> int:
        return df['amount'].mean()

if __name__ == '__main__':
    transformer = Transformer()
    data = transformer.read_orders()

    countries = ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']
    data = transformer.enrich_orders(data, 'Country', countries)

    threshold = 599  # Change this value
    low_spending_customers, high_spending_customers = transformer.split_customers(data, threshold)

