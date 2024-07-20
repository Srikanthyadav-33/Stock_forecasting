# fetch_data.py
import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def fetch_stock_data(symbol, api_key, interval='1min', outputsize='full'):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)
    return data

if __name__ == "__main__":
    api_key = os.getenv('ALPHAVANTAGE_API_KEY')  # Ensure your API key is set in the environment variable
    if not api_key:
        api_key = 'D8JSR6E36XSXZQ09'  # Directly set your API key here if environment variable is not found

    symbol = 'GOOGL'  # Change this to the stock symbol you want to fetch
    data = fetch_stock_data(symbol, api_key)
    data.to_csv(f'{symbol}_intraday.csv')
    print(f"Data for {symbol} saved to {symbol}_intraday.csv")
