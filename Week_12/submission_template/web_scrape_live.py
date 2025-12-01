"""
Task 2: Web Scraping from Live Websites
This script demonstrates how to extract data from a live website.
Note: Always check robots.txt and terms of service before scraping.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website (using a practice site designed for scraping)
url = 'http://quotes.toscrape.com/'

# Add headers to identify the scraper
headers = {
    'User-Agent': 'Mozilla/5.0 (Educational Purpose - Data Science Lab)',
    'Accept': 'text/html,application/xhtml+xml',
}

print("=== Scraping Quotes from Quotes to Scrape ===")

# Send GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all quote elements
    quotes = soup.find_all('div', class_='quote')
    
    # Extract data
    data = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        data.append({
            'quote': text,
            'author': author,
            'tags': ', '.join(tags)
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    print(f"Extracted {len(df)} quotes from page 1")
    print("\nFirst 5 quotes:")
    print(df.head())
    
    # Save to CSV
    df.to_csv('quotes.csv', index=False)
    print("\nData saved to quotes.csv")
    
    # Optional: Extract from multiple pages
    print("\n=== Extracting from Multiple Pages ===")
    all_quotes = data.copy()
    base_url = 'http://quotes.toscrape.com/page/'
    
    for page in range(2, 6):  # Pages 2-5
        page_url = f'{base_url}{page}/'
        time.sleep(1)  # Be respectful - add delay between requests
        
        response = requests.get(page_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                all_quotes.append({
                    'quote': text,
                    'author': author,
                    'tags': ', '.join(tags)
                })
            print(f"Extracted quotes from page {page}")
        else:
            print(f"Failed to retrieve page {page}")
    
    # Create DataFrame with all quotes
    df_all = pd.DataFrame(all_quotes)
    print(f"\nTotal quotes extracted: {len(df_all)}")
    df_all.to_csv('quotes_all.csv', index=False)
    print("All quotes saved to quotes_all.csv")
    
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

