import pandas as pd
import talib
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
    # Load the data
    data = pd.read_csv(file_path)
    
    # Convert the Date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Calculate Moving Averages
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)

    # Calculate RSI
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

    # Calculate MACD
    data['MACD'], data['MACD_Signal'], _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    # Print the stock symbol and a summary of the calculated indicators
    stock_symbol = os.path.basename(file_path).split('_')[0]  # Extract the stock symbol from the file name
    print(f"{stock_symbol} Indicators:")
    print(data[['Close', 'SMA_50', 'SMA_200', 'RSI', 'MACD', 'MACD_Signal']].tail(), "\n")