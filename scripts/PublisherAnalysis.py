import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import nltk
from datetime import datetime

# Ensure NLTK is ready
nltk.download('vader_lexicon')

# Load dataset
df = pd.read_csv("C:/Users/hp/Documents/raw_analyst_ratings.csv")



# -------------------------------------------
# 4. Publisher Analysis

# A. Most Active Publishers
# Count how many articles each publisher has contributed
top_publishers = df['publisher'].value_counts().head(10)  # Top 10 publishers

# B. Extract domains from email addresses if present in publisher name
# If publisher name contains an email, we'll extract the domain part
def extract_domain(publisher):
    if '@' in str(publisher):  # Check if email address exists
        return publisher.split('@')[1]
    return 'No Domain'  # If not an email, return 'No Domain'

# Apply the function to extract domains
df['publisher_domain'] = df['publisher'].apply(extract_domain)

# C. Frequency of Publications by Domain
publisher_domains = df['publisher_domain'].value_counts().head(10)  # Top 10 publisher domains

# -------------------------------------------
# Visualization: Plotting the Publisher Analysis

# Plot the top publishers (Most Active Publishers)
plt.figure(figsize=(10, 6))
top_publishers.plot(kind='barh', color='teal')
plt.title('Top 10 Most Active Publishers', fontsize=14)
plt.xlabel('Number of Articles', fontsize=12)
plt.ylabel('Publisher', fontsize=12)
plt.grid(True, axis='x')
plt.tight_layout()
plt.show()

# Plot the top publishers' domains (Most Common Domains)
plt.figure(figsize=(10, 6))
publisher_domains.plot(kind='barh', color='purple')
plt.title('Top 10 Most Common Publisher Domains', fontsize=14)
plt.xlabel('Number of Articles', fontsize=12)
plt.ylabel('Publisher Domain', fontsize=12)
plt.grid(True, axis='x')
plt.tight_layout()
plt.show()

# -------------------------------------------
# Display Results in Terminal

# 1. Most Active Publishers
print("="*50)
print("Most Active Publishers (Top 10):")
print(top_publishers)
print("="*50)

# 2. Most Common Publisher Domains
print("Most Common Publisher Domains (Top 10):")
print(publisher_domains)
print("="*50)
