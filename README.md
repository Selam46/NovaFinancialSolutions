# NovaFinancialSolutions
## Financial News EDA and Analysis

This project performs **Exploratory Data Analysis (EDA)** and **Text Analysis** on a financial news dataset to gain insights into the articles, publishers, and sentiments. Additionally, it conducts quantitative analysis on stock market data to explore financial metrics and indicators using historical price data.

### Project Overview
The project includes several key analyses:

#### 1. Financial News Analysis
- **Descriptive Statistics**: Basic statistics on headline lengths, publisher activity, and publication dates.
- **Sentiment Analysis**: Perform sentiment analysis on news headlines to classify sentiment as positive, negative, or neutral.
- **Topic Modeling and Keyword Extraction**: Identify frequent terms and significant events in the headlines.
- **Time Series Analysis**: Analyze publication frequency over time and visualize trends.
- **Publisher Analysis**: Identify which publishers contribute most to the news feed and extract domains from email addresses if present in publisher names.

#### 2. Stock Market Data Analysis
- **Data Loading and Preparation**: Load historical stock price data from CSV files and prepare it for analysis.
- **Technical Indicators**: Calculate various technical indicators such as Moving Averages (SMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD) using TA-Lib.
- **Financial Metrics**: Use PyNance (or yfinance) to retrieve and analyze financial metrics of different stocks.
- **Data Visualization**: Create visualizations to understand stock price movements, technical indicators, and trends over time.

### Dependencies

To run the project, you'll need to install the following libraries:

- `pandas` - For data manipulation
- `numpy` - For numerical operations
- `matplotlib` - For plotting graphs
- `seaborn` - For advanced visualizations
- `nltk` - For natural language processing (sentiment analysis, tokenization)
- `sklearn` - For feature extraction and text vectorization
- `wordcloud` - For generating word clouds from the text data
- `TA-Lib` - For calculating technical indicators
- `yfinance` - For fetching financial data (if using yfinance)
- `datetime` - For handling date and time operations

Install the required libraries using `pip`:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn wordcloud TA-Lib yfinance