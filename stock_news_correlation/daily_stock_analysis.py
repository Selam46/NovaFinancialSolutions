import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from textblob import TextBlob

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

        # Calculate daily stock returns
        df['daily_return'] = df['Close'].pct_change() * 100

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

# Step 4: Conduct Sentiment Analysis on Headlines
def analyze_sentiment(headline):
    blob = TextBlob(headline)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

news_df['sentiment'] = news_df['headline'].apply(analyze_sentiment)

# Step 5: Save the Resulting DataFrame
aligned_df = pd.DataFrame(aligned_data)
aligned_df['sentiment'] = aligned_df['headline'].apply(analyze_sentiment)

output_path = "C:\\Users\\hp\\Documents\\aligned_news_stock_data_with_sentiment.csv"
aligned_df.to_csv(output_path, index=False)

print(f"Aligned data with sentiment saved to {output_path}")

# Step 6: Correlation Analysis
# Calculate correlation between sentiment and daily stock returns
correlation_results = {}
for ticker, df in stock_data.items():
    if ticker in aligned_df['stock'].unique():
        ticker_data = aligned_df[aligned_df['stock'] == ticker]
        sentiment_scores = ticker_data['sentiment'].map({
            'positive': 1,
            'neutral': 0,
            'negative': -1
        })
        returns = ticker_data['daily_return']

        # Compute correlation
        correlation = sentiment_scores.corr(returns)
        correlation_results[ticker] = correlation

# Save correlation results
correlation_output_path = "C:\\Users\\hp\\Documents\\sentiment_stock_correlation.csv"
pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Correlation']).to_csv(correlation_output_path)

print(f"Correlation results saved to {correlation_output_path}")

# Visualization 1: Stock Closing Prices and Daily Returns
for ticker, df in stock_data.items():
    plt.figure(figsize=(14, 6))
    
    # Closing prices
    plt.subplot(2, 1, 1)
    plt.plot(df['Date'], df['Close'], label=f'{ticker} Close Price', color='blue')
    plt.title(f'{ticker} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    
    # Daily returns
    plt.subplot(2, 1, 2)
    plt.plot(df['Date'], df['daily_return'], label=f'{ticker} Daily Returns', color='green')
    plt.title(f'{ticker} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return (%)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Visualization 2: Sentiment Distribution
plt.figure(figsize=(8, 5))
sentiment_counts = news_df['sentiment'].value_counts()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Visualization 3: Correlation Heatmap
correlation_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Correlation'])
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_df, annot=True, cmap='coolwarm', cbar=True, fmt=".2f")
plt.title("Sentiment vs. Daily Return Correlation Heatmap")
plt.xlabel("Stock")
plt.ylabel("Correlation")
plt.show()
