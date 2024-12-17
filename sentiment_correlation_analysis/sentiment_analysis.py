import pandas as pd
import os
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

class SentimentAnalysis:
    """
    Class to perform sentiment analysis on news headlines:
    - Align news dates with stock trading days.
    - Conduct sentiment analysis.
    - Visualize sentiment results.
    """
    def __init__(self, news_path, stock_files, output_path):
        self.news_path = news_path
        self.stock_files = stock_files
        self.output_path = output_path
        self.news_df = None
        self.stock_data = {}
        self.aligned_data = []

    def load_news_data(self):
        """Load and preprocess news data."""
        try:
            self.news_df = pd.read_csv(self.news_path)
            if 'date' not in self.news_df.columns or 'headline' not in self.news_df.columns:
                raise KeyError("Required columns ('date', 'headline') are missing in the news data.")

            self.news_df['date'] = pd.to_datetime(self.news_df['date'], errors='coerce')
            self.news_df.dropna(subset=['date'], inplace=True)

            # Localize to UTC
            if self.news_df['date'].dt.tz is None:
                self.news_df['date'] = self.news_df['date'].dt.tz_localize('UTC')
            else:
                self.news_df['date'] = self.news_df['date'].dt.tz_convert('UTC')

            print("News data loaded and processed successfully.")

        except Exception as e:
            print(f"Error loading news data: {e}")
            raise

    def load_stock_data(self):
        """Load and preprocess stock data."""
        try:
            for file in self.stock_files:
                ticker = os.path.basename(file).split('_')[0]  # Extract ticker from filename
                df = pd.read_csv(file)

                if 'Date' not in df.columns:
                    print(f"Warning: 'Date' column is missing in {file}. Skipping...")
                    continue

                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                df.dropna(subset=['Date'], inplace=True)
                df.sort_values('Date', inplace=True)

                # Localize dates to UTC
                if df['Date'].dt.tz is None:
                    df['Date'] = df['Date'].dt.tz_localize('UTC')
                else:
                    df['Date'] = df['Date'].dt.tz_convert('UTC')

                self.stock_data[ticker] = df
            print("Stock data loaded and processed successfully.")

        except Exception as e:
            print(f"Error loading stock data: {e}")
            raise

    def analyze_sentiment(self, headline):
        """Analyze sentiment of a headline using TextBlob."""
        try:
            blob = TextBlob(headline)
            polarity = blob.sentiment.polarity
            if polarity > 0:
                return 'positive'
            elif polarity < 0:
                return 'negative'
            else:
                return 'neutral'
        except Exception as e:
            print(f"Error analyzing sentiment for headline: {headline}. Error: {e}")
            return 'neutral'

    def align_data(self):
        """Align news data to the closest stock trading day."""
        try:
            for _, news_row in self.news_df.iterrows():
                ticker = news_row.get('stock')
                news_date = news_row['date']

                if ticker in self.stock_data:
                    stock_df = self.stock_data[ticker]
                    trading_days = stock_df['Date']
                    matching_date = trading_days[trading_days <= news_date].max()

                    if pd.notna(matching_date):
                        stock_row = stock_df[stock_df['Date'] == matching_date].iloc[0]
                        aligned_row = {
                            **news_row.to_dict(),
                            **stock_row.to_dict()
                        }
                        aligned_row['sentiment'] = self.analyze_sentiment(news_row['headline'])
                        self.aligned_data.append(aligned_row)

            aligned_df = pd.DataFrame(self.aligned_data)
            aligned_df.to_csv(self.output_path, index=False)
            print(f"Aligned data with sentiment saved to {self.output_path}")

            return aligned_df

        except Exception as e:
            print(f"Error aligning data: {e}")
            raise

    def visualize_sentiment_distribution(self):
        """Plot sentiment distribution of news headlines."""
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.news_df, x='sentiment', palette='viridis')
        plt.title('Sentiment Distribution of Headlines', fontsize=16)
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.tight_layout()
        plt.show()

    def visualize_sentiment_per_stock(self, aligned_df):
        """Plot sentiment counts for each stock."""
        plt.figure(figsize=(12, 6))
        sns.countplot(data=aligned_df, x='stock', hue='sentiment', palette='viridis')
        plt.title('Sentiment Analysis for Each Stock', fontsize=16)
        plt.xlabel('Stock', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Sentiment')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Define file paths
    news_path = "C:\\Users\\hp\\Documents\\raw_analyst_ratings.csv"
    stock_files = [
        "C:\\Users\\hp\\Documents\\yfinance_data\\NVDA_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\TSLA_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\AAPL_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\AMZN_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\GOOG_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\META_historical_data.csv",
        "C:\\Users\\hp\\Documents\\yfinance_data\\MSFT_historical_data.csv"
    ]
    output_path = "C:\\Users\\hp\\Documents\\aligned_news_stock_data_with_sentiment.csv"

    # Initialize and execute sentiment analysis
    sentiment_analyzer = SentimentAnalysis(news_path, stock_files, output_path)
    
    # Step 1: Load data
    sentiment_analyzer.load_news_data()
    sentiment_analyzer.load_stock_data()

    # Step 2: Align and analyze sentiment
    sentiment_analyzer.news_df['sentiment'] = sentiment_analyzer.news_df['headline'].apply(
        sentiment_analyzer.analyze_sentiment)
    aligned_df = sentiment_analyzer.align_data()

    # Step 3: Visualization
    sentiment_analyzer.visualize_sentiment_distribution()
    sentiment_analyzer.visualize_sentiment_per_stock(aligned_df)
