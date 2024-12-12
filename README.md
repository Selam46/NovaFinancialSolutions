# NovaFinancialSolutions
# Financial News EDA and Analysis

This project performs **Exploratory Data Analysis (EDA)** and **Text Analysis** on a financial news dataset to gain insights into the articles, publishers, and sentiments. The dataset consists of financial news headlines and related metadata, which we analyze to uncover trends in publishing frequency, sentiment, and keywords.

### Project Overview
The project includes several key analyses:
- **Descriptive Statistics**: Basic statistics on headline lengths, publisher activity, and publication dates.
- **Sentiment Analysis**: Perform sentiment analysis on news headlines to classify sentiment as positive, negative, or neutral.
- **Topic Modeling and Keyword Extraction**: Identify frequent terms and significant events in the headlines.
- **Time Series Analysis**: Analyze publication frequency over time and visualize trends.
- **Publisher Analysis**: Identify which publishers contribute most to the news feed and extract domains from email addresses if present in publisher names.

### Dependencies

To run the project, you'll need to install the following libraries:

- `pandas` - For data manipulation
- `numpy` - For numerical operations
- `matplotlib` - For plotting graphs
- `seaborn` - For advanced visualizations
- `nltk` - For natural language processing (sentiment analysis, tokenization)
- `sklearn` - For feature extraction and text vectorization
- `wordcloud` - For generating word clouds from the text data
- `datetime` - For handling date and time operations

Install the required libraries using `pip`:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn wordcloud
