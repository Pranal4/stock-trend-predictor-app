import yfinance as yf
import pandas as pd
import os

# --- Configuration ---
TICKER = "RELIANCE.NS"
START_DATE = "2020-01-01"
END_DATE = "2024-12-31"
DATA_PATH = "data"
RAW_DATA_FILE = os.path.join(DATA_PATH, f"{TICKER}_raw_data.csv")

# --- Data Fetching ---
def fetch_stock_data(ticker, start, end, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    print(f"Fetching data for {ticker} from {start} to {end}...")
    stock_data = yf.download(ticker, start=start, end=end)
    if stock_data.empty:
        print(f"No data found for {ticker}.")
        return
    stock_data.to_csv(filepath)
    print(f"Data saved successfully to {filepath}")
    print("\nData Head:")
    print(stock_data.head())

if __name__ == "__main__":
    fetch_stock_data(TICKER, START_DATE, END_DATE, RAW_DATA_FILE)
