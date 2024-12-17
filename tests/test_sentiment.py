import unittest
from stock_news_correlation.daily_stock_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        self.assertEqual(analyze_sentiment("The stock prices are soaring!"), 'positive')

    def test_negative_sentiment(self):
        self.assertEqual(analyze_sentiment("Stock prices have plummeted drastically."), 'negative')

    def test_neutral_sentiment(self):
        self.assertEqual(analyze_sentiment("Stock market closed today."), 'neutral')

    def test_empty_headline(self):
        self.assertEqual(analyze_sentiment(""), 'neutral')  # Edge case: empty headline

if __name__ == '__main__':
    unittest.main()
