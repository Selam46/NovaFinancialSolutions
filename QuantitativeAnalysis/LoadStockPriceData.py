import pandas as pd

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

# Loop through each CSV file
for file_path in csv_files:
    # Load the data
    df = pd.read_csv(file_path)
    
    # Convert the Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set the Date column as the index
    df.set_index('Date', inplace=True)
    
    # Optionally, store the DataFrame in a dictionary with the stock symbol as the key
    stock_symbol = file_path.split('\\')[-1].split('_')[0]  # Extract stock symbol
    dataframes[stock_symbol] = df

    # Display the first few rows of the DataFrame
    print(f"{stock_symbol} Data:")
    print(df.head(), "\n")

# Now you can access each DataFrame using dataframes['AAPL'], dataframes['AMZN'], etc.