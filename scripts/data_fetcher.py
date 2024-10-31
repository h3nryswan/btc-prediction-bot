# scripts/data_fetcher.py
import yfinance as yf
import pandas as pd

def fetch_btc_data(start_date="2015-01-01", end_date="2023-12-31", interval="1d"):
    # Fetches Bitcoin data from Yahoo Finance
    btc = yf.Ticker("BTC-USD")
    data = btc.history(start=start_date, end=end_date, interval=interval)
    
    # Keep only relevant columns
    data = data[["Open", "High", "Low", "Close", "Volume"]]
    data.reset_index(inplace=True)  # Convert the index to a regular column for easier handling
    data.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    
    # Save to CSV
    data.to_csv("data/btc_data.csv", index=False)
    print("Bitcoin data fetched and saved to data/btc_data.csv")

if __name__ == "__main__":
    fetch_btc_data()

