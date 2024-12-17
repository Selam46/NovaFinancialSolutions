import pandas as pd
import os
from datetime import datetime, timedelta
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

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

# Display the output in the terminal instead of saving to a file
print("Aligned data with sentiment:")
print(aligned_df.head())  # Display first few rows in the terminal

# Step 6: Aggregate Sentiments
# Compute average daily sentiment scores for each stock
aligned_df['sentiment_score'] = aligned_df['sentiment'].map({
    'positive': 1,
    'neutral': 0,
    'negative': -1
})

average_sentiment = aligned_df.groupby(['stock', 'Date']).agg(
    avg_sentiment=('sentiment_score', 'mean')
).reset_index()

# Display the aggregated sentiment data
print("\nAggregated Sentiment Data:")
print(average_sentiment.head())  # Display first few rows in the terminal

# Step 7: Correlation Analysis
# Merge average sentiment with stock daily returns
correlation_results = {}
for ticker, df in stock_data.items():
    if ticker in average_sentiment['stock'].unique():
        sentiment_data = average_sentiment[average_sentiment['stock'] == ticker]
        stock_returns = df[['Date', 'daily_return']]

        # Merge on date
        merged_data = pd.merge(sentiment_data, stock_returns, on='Date', how='inner')

        # Check if merged data has enough valid rows to compute correlation
        if len(merged_data) > 1:  # Ensure there are at least 2 data points
            # Calculate Pearson correlation coefficient
            correlation = merged_data['avg_sentiment'].corr(merged_data['daily_return'])
            correlation_results[ticker] = correlation
        else:
            print(f"Not enough data to compute correlation for {ticker}.")

plt.figure(figsize=(8, 5))
sentiment_counts = news_df['sentiment'].value_counts()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

# Step 6: Visualize Stock Daily Returns
for ticker, df in stock_data.items():
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['daily_return'], label=f'{ticker} Daily Returns', color='green')
    plt.title(f'{ticker} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return (%)')
    plt.legend()
    plt.show()

# Step 7: Visualize Aggregated Sentiments
for ticker in average_sentiment['stock'].unique():
    stock_sentiment = average_sentiment[average_sentiment['stock'] == ticker]
    plt.figure(figsize=(14, 6))
    plt.plot(stock_sentiment['Date'], stock_sentiment['avg_sentiment'], label=f'{ticker} Avg Sentiment', color='blue')
    plt.title(f'Average Daily Sentiment for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Average Sentiment')
    plt.legend()
    plt.show()

# Step 8: Visualize Correlation with Scatter Plots
for ticker, df in stock_data.items():
    if ticker in correlation_results:
        sentiment_data = average_sentiment[average_sentiment['stock'] == ticker]
        stock_returns = df[['Date', 'daily_return']]
        
        # Merge on date
        merged_data = pd.merge(sentiment_data, stock_returns, on='Date', how='inner')
        
        if len(merged_data) > 1:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=merged_data['avg_sentiment'], y=merged_data['daily_return'], color='purple')
            plt.title(f'Sentiment vs. Daily Returns for {ticker}')
            plt.xlabel('Average Sentiment')
            plt.ylabel('Daily Return (%)')
            plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
            plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
            plt.show()

# Display the correlation results 
print("\nCorrelation Results:")
for ticker, correlation in correlation_results.items():
    print(f"{ticker}: {correlation}")

print("\nCorrelation results are displayed above.")
