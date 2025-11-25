# analyze.py - Simple data analysis script
import pandas as pd
import sys

# Read CSV file
df = pd.read_csv('data/scores.csv')

# Calculate statistics
print("Score Statistics:")
print(f"Mean: {df['Score'].mean():.2f}")
print(f"Max: {df['Score'].max()}")
print(f"Min: {df['Score'].min()}")
print(f"Count: {len(df)}")

