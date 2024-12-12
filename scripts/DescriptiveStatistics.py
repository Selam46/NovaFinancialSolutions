import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load dataset
df = pd.read_csv("C:/Users/hp/Documents/raw_analyst_ratings.csv")

# -------------------------------------------
# 1. Descriptive Statistics

# A. Basic statistics for headline lengths
df['headline_length'] = df['headline'].apply(lambda x: len(str(x)))

# Descriptive statistics for headline length
headline_stats = df['headline_length'].describe()

# Displaying the headline length statistics
print("\n" + "="*50)
print("Descriptive Statistics for Headline Length:")
print(headline_stats)
print("\n" + "="*50)

# Plotting the distribution of headline lengths (Histogram with KDE)
plt.figure(figsize=(10, 6))
sns.histplot(df['headline_length'], kde=True, bins=50, color='blue')
plt.title('Distribution of Headline Lengths')
plt.xlabel('Headline Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# B. Number of articles per publisher
publisher_counts = df['publisher'].value_counts()

# Displaying the top 10 most active publishers
print("Top Publishers (Most Active):")
print(publisher_counts.head(10))
print("\n" + "="*50)

# Plotting the top publishers (Bar chart)
plt.figure(figsize=(10, 6))
publisher_counts.head(10).plot(kind='bar', color='lightblue')
plt.title('Top 10 Publishers by Number of Articles')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(True)
plt.show()

# C. Publication date trends
# Convert 'date' column to datetime format (if not already in datetime format)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Checking for any invalid dates
invalid_dates = df[df['date'].isna()]
print("Rows with invalid date format (if any):")
print(invalid_dates)

# Analyzing the publication date distribution
date_counts = df['date'].value_counts().sort_index()

# Displaying a sample of the publication date distribution
print("Publication Date Distribution (Sample):")
print(date_counts.head())  # Displaying a sample of publication dates
print("\n" + "="*50)

# Plotting the publication frequency over time (Line plot)
plt.figure(figsize=(12, 6))
date_counts.plot(kind='line', color='purple')
plt.title('Publication Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------
