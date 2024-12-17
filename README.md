# Nova Financial Solutions

## Overview

Nova Financial Solutions is a data-driven project that analyzes the relationship between financial news and stock market movements. It includes **exploratory data analysis**, **quantitative analysis**, and **correlation analysis** to uncover patterns and insights using Python tools and libraries.

## Objectives

- Perform **Exploratory Data Analysis (EDA)** on financial news datasets.
- Analyze stock price data with technical indicators using **TA-Lib** and **PyNance**.
- Identify correlations between news sentiment and stock price movements.

## Directory Structure

```plaintext
NovaFinancialSolutions/
├── .github/                 # CI/CD workflows
├── .vscode/                 # VS Code settings
├── notebooks/               # Jupyter Notebooks for EDA and analysis
│   ├── exploratory_analysis.ipynb
│   └── news_stock_correlation.ipynb
├── news-analysis/           # News dataset analysis modules
│   ├── PublisherAnalysis.py
│   ├── TestAnalysis.py
│   └── TimeSeriesAnalysis.py
├── QuantitativeAnalysis/    # Stock price quantitative analysis
│   ├── FinancialMetrics.py
│   ├── LoadStockPrices.py
│   ├── TechnicalIndicators.py
│   └── Visualization.py
├── stock-news-correlation/  # Correlation between news sentiment and stock prices
│   ├── daily_stock_analysis.py
│   ├── data_processing.py
│   ├── sentiment_analysis.py
│   └── correlation_analysis.py
├── tests/                   # Unit tests
│   ├── test_sentiment_analysis.py
│   └── test_data_processing.py
├── .gitignore               # Git ignored files
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation

## Setup Instructions
Clone the Repository
git clone https://github.com/Selam46/NovaFinancialSolutions.git
cd NovaFinancialSolutions

### Create a Virtual Environment and Install Dependencies

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### Key Tools and Libraries
pandas, numpy: Data manipulation
TA-Lib, PyNance: Technical indicators and financial metrics
nltk, TextBlob: Sentiment analysis
matplotlib, seaborn: Data visualization
pytest: Unit testing framework
```
