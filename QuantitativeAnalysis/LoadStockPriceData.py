import pandas as pd
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

def load_stock_data(file_path):
    """
    Load stock price data from a CSV file, validate, and preprocess it.

    Args:
        file_path (str): Full path to the CSV file.

    Returns:
        pd.DataFrame: Preprocessed DataFrame or None if an error occurs.
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: File not found at {file_path}")
        
        # Load the data
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ['Date', 'Close']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Missing required columns {required_columns} in {file_path}")

        # Convert Date column to datetime and set as index
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])  # Drop rows with invalid dates
        df.set_index('Date', inplace=True)

        # Calculate daily stock returns
        df['daily_return'] = df['Close'].pct_change() * 100

        print(f"Successfully processed {len(df)} rows from {file_path}")
        return df

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


if __name__ == "__main__":
    # Loop through each CSV file
    for file_path in csv_files:
        # Extract stock symbol from the file path
        stock_symbol = os.path.basename(file_path).split('_')[0]

        # Load and process data
        df = load_stock_data(file_path)
        if df is not None:
            dataframes[stock_symbol] = df

            # Display the first few rows
            print(f"\n{stock_symbol} Data:")
            print(df.head(), "\n")
        else:
            print(f"Failed to process data for {stock_symbol}.\n")
