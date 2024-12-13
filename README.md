# Nova Financial Solutions

## Overview

Nova Financial Solutions is a project aimed at providing tools for analyzing financial data. This includes quantitative analysis, visualization of stock prices, and technical indicators. The project leverages various libraries to facilitate data processing and analysis.

## Objectives

- Perform quantitative analysis on stock data.
- Visualize stock price trends and technical indicators.
- Provide tools for data preprocessing and analysis.

## Directory Structure

````plaintext
├── .github/               # GitHub workflows for CI/CD
├── .venv/                 # Virtual environment for package management
├── .vscode/               # VS Code settings for the project
├── notebooks/             # Jupyter notebooks for analysis
│   ├── exploratory_analysis.ipynb  # EDA on financial news dataset
├── QuantitativeAnalysis/   # Main package for quantitative analysis
│   ├── __init__.py        # Package initialization
│   ├── FinancialMetrics.py # Module for calculating financial metrics
│   ├── LoadStockPrices.py  # Module for loading stock price data
│   ├── TechnicalIndicators.py # Module for technical indicators analysis
│   └── Visualization.py    # Module for visualizing data
├── scripts/               # Utility scripts for various tasks
│   ├── __init__.py        # Package initialization
│   ├── PublisherAnalysis.py # Script for analyzing publishers
│   ├── TestAnalysis.py     # Script for conducting tests
│   └── TimeSeriesAnalysis.py # Script for time series analysis
├── tests/                 # Unit tests for the project
│   ├── __init__.py        # Package initialization
│   └── test_financial_metrics.py  # Tests for FinancialMetrics module
├── .gitignore             # Files and directories to ignore in Git
├── README.md              # Project documentation
└── requirements.txt       # Required Python libraries


### Set up Instructions
Step 1: Clone the Repository

git clone https://github.com/Selam46/solar-radiation-study.git

cd solar-radiation-study

Step 2: Install Dependencies

Create a virtual environment and install required packages:

python3 -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate

To run the project,Install the required libraries using `pip`:

```bash
pip install nltk scikit-learn wordcloud TA-Lib yfinance

pip install -r requirements.txt

````
