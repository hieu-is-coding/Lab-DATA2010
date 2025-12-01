"""
Task 3: API Data Extraction
This script demonstrates how to extract data from REST APIs using the requests library.
"""

import requests
import pandas as pd
import json

print("=== Example 1: JSONPlaceholder API ===")
# JSONPlaceholder API - Fake REST API for testing
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(f"Extracted {len(df)} posts")
    print(df.head())
    df.to_csv('posts.csv', index=False)
    print("Data saved to posts.csv\n")
else:
    print(f"Error: {response.status_code}\n")

print("=== Example 2: REST Countries API ===")
# REST Countries API - Country information
url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)

if response.status_code == 200:
    countries = response.json()
    # Extract specific fields
    country_data = []
    for country in countries[:20]:  # First 20 countries
        country_data.append({
            'name': country.get('name', {}).get('common', 'N/A'),
            'capital': country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A',
            'population': country.get('population', 0),
            'region': country.get('region', 'N/A')
        })
    df_countries = pd.DataFrame(country_data)
    print(f"Extracted {len(df_countries)} countries")
    print(df_countries.head(10))
    df_countries.to_csv('countries.csv', index=False)
    print("Data saved to countries.csv")
else:
    print(f"Error: {response.status_code}")

