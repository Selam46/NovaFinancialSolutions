import pandas as pd
import yfinance as yf
import os

# Define the list of CSV files
csv_files = [
    r'C:\Users\hp\Documents\yfinance_data\AAPL_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\AMZN_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\GOOG_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\META_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\MSFT_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\NVDA_historical_data.csv',
    r'C:\Users\hp\Documents\yfinance_data\TSLA_historical_data.csv'
]

# Loop through each CSV file
for file_path in csv_files:
    # Extract stock symbol from the file name
    stock_symbol = os.path.basename(file_path).split('_')[0]  # e.g., 'AAPL'

    # Fetch financial metrics using yfinance
    stock = yf.Ticker(stock_symbol)

    # Get financial metrics
    try:
        financials = stock.financials
        print(f"{stock_symbol} Financial Metrics:")
        print(financials)
        print("\n" + "="*50 + "\n")  # Separator for clarity
    except Exception as e:
        print(f"Error retrieving data for {stock_symbol}: {e}")