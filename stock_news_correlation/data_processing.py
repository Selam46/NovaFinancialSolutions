import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Step 1: Load News Data
news_path = "C:\\Users\\hp\\Documents\\raw_analyst_ratings.csv"
news_df = pd.read_csv(news_path)

# Check if 'date' column exists in news data
if 'date' in news_df.columns:
    # Convert `date` column to datetime and ensure consistency
    news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
    if news_df['date'].dt.tz is None:
        news_df['date'] = news_df['date'].dt.tz_localize('UTC')
    else:
        news_df['date'] = news_df['date'].dt.tz_convert('UTC')
else:
    raise KeyError("The 'date' column is missing in the news data.")

# Step 2: Load Stock Data
stock_files = [
    "C:\\Users\\hp\\Documents\\yfinance_data\\NVDA_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\TSLA_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\AAPL_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\AMZN_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\GOOG_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\META_historical_data.csv",
    "C:\\Users\\hp\\Documents\\yfinance_data\\MSFT_historical_data.csv"
]

stock_data = {}
for file in stock_files:
    ticker = os.path.basename(file).split('_')[0]  # Extract ticker from filename
    df = pd.read_csv(file)

    # Check if 'Date' column exists in stock data
    if 'Date' in df.columns:
        # Fix date column
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Drop rows with invalid dates
        df = df.dropna(subset=['Date'])

        # Sort by date
        df = df.sort_values('Date')

        # Localize dates to UTC for consistency
        if df['Date'].dt.tz is None:
            df['Date'] = df['Date'].dt.tz_localize('UTC')
        else:
            df['Date'] = df['Date'].dt.tz_convert('UTC')

        stock_data[ticker] = df
    else:
        print(f"Warning: The 'Date' column is missing in the stock data for {ticker}. Skipping this file.")
        continue

# Step 3: Match News Dates to Stock Trading Days
aligned_data = []
for _, news_row in news_df.iterrows():
    ticker = news_row['stock']
    news_date = news_row['date']

    if ticker in stock_data:
        stock_df = stock_data[ticker]

        # Find the closest prior trading day
        trading_days = stock_df['Date']
        matching_date = trading_days[trading_days <= news_date].max()

        if pd.notna(matching_date):
            # Get the stock data for the matching date
            stock_row = stock_df[stock_df['Date'] == matching_date].iloc[0]

            # Combine news and stock data
            aligned_row = {
                **news_row.to_dict(),
                **stock_row.to_dict()
            }
            aligned_data.append(aligned_row)

# Step 4: Create and Save the Result DataFrame
aligned_df = pd.DataFrame(aligned_data)
output_path = "C:\\Users\\hp\\Documents\\aligned_news_stock_data.csv"
aligned_df.to_csv(output_path, index=False)

print(f"Aligned data saved to {output_path}")

# Step 5: Visualization

# Plot 1: Number of news articles per stock
plt.figure(figsize=(10, 6))
sns.countplot(data=news_df, x='stock', palette='viridis')
plt.title('Number of News Articles per Stock', fontsize=16)
plt.xlabel('Stock', fontsize=12)
plt.ylabel('Number of Articles', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
# plt.savefig("C:\\Users\\hp\\Documents\\news_articles_per_stock.png")
plt.show()

# Plot 2: Stock price trends over time (e.g., closing price)
for ticker, df in stock_data.items():
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label=ticker)
    plt.title(f'{ticker} Stock Price Trend', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Closing Price', fontsize=12)
    plt.legend()
    plt.tight_layout()
    # plt.savefig(f"C:\\Users\\hp\\Documents\\{ticker}_price_trend.png")
    plt.show()

# Plot 3: Distribution of closing prices
plt.figure(figsize=(10, 6))
for ticker, df in stock_data.items():
    sns.histplot(df['Close'], label=ticker, kde=True, binwidth=5, alpha=0.6)
plt.title('Distribution of Closing Prices', fontsize=16)
plt.xlabel('Closing Price', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(title='Stock')
plt.tight_layout()
# plt.savefig("C:\\Users\\hp\\Documents\\closing_price_distribution.png")
plt.show()
