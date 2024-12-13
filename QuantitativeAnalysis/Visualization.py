import pandas as pd
import matplotlib.pyplot as plt
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

# Initialize a dictionary to hold DataFrames
dataframes = {}

# Load data and prepare DataFrames
for file_path in csv_files:
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    stock_symbol = os.path.basename(file_path).split('_')[0]
    dataframes[stock_symbol] = df

# Visualization
for stock_symbol, df in dataframes.items():
    plt.figure(figsize=(14, 7))
    
    # Plot the closing price
    plt.plot(df['Close'], label='Close Price', color='blue')
    
    # Plot moving averages if they exist
    if 'SMA_50' in df.columns and 'SMA_200' in df.columns:
        plt.plot(df['SMA_50'], label='50-Day SMA', color='orange')
        plt.plot(df['SMA_200'], label='200-Day SMA', color='red')
    
    plt.title(f'{stock_symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()