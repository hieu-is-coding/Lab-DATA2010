# Week 12 - Data Extraction Lab Submission

This project demonstrates various data extraction techniques including web scraping, API extraction, file parsing, and database queries.

## What This Project Does

This project contains scripts for:
1. **Web Scraping** - Extracting data from HTML pages (both static and dynamic)
2. **API Extraction** - Retrieving data from REST APIs
3. **File Parsing** - Extracting data from CSV, JSON, XML, and PDF files
4. **Database Extraction** - Querying SQL databases
5. **Data Pipeline** - Combining data from multiple sources

## Prerequisites

Install required Python packages:
```bash
pip install -r requirements.txt
```

For Selenium (Task 6), you may also need:
- ChromeDriver or GeckoDriver
- Download from: https://chromedriver.chromium.org/ or https://github.com/mozilla/geckodriver/releases

## Project Structure

```
.
├── web_scrape_basic.py          # Task 1: Basic HTML scraping
├── web_scrape_live.py           # Task 2: Live website scraping
├── api_extract.py                # Task 3: API data extraction
├── file_extract.py               # Task 4: File format extraction
├── db_extract.py                 # Task 5: Database extraction
├── dynamic_scrape.py             # Task 6: Dynamic content (if applicable)
├── extraction_pipeline.py        # Task 7: Data extraction pipeline
├── ethical_scraping.py           # Task 8: Ethical practices
├── sample.html                   # Sample HTML file
├── data.json                     # Sample JSON file
├── data.xml                      # Sample XML file
├── sample.db                     # SQLite database
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## How to Run

### Task 1: Basic HTML Scraping
```bash
python web_scrape_basic.py
```

### Task 2: Live Website Scraping
```bash
python web_scrape_live.py
```

### Task 3: API Extraction
```bash
python api_extract.py
```

### Task 4: File Format Extraction
```bash
python file_extract.py
```

### Task 5: Database Extraction
```bash
python db_extract.py
```

### Task 6: Dynamic Content (if applicable)
```bash
python dynamic_scrape.py
```

### Task 7: Data Extraction Pipeline
```bash
python extraction_pipeline.py
```

### Task 8: Ethical Scraping Practices
```bash
python ethical_scraping.py
```

## Data Sources Used

- **Web Scraping**: [Quotes to Scrape](http://quotes.toscrape.com/) - Practice site for web scraping
- **APIs**: 
  - JSONPlaceholder API (https://jsonplaceholder.typicode.com/)
  - REST Countries API (https://restcountries.com/)
- **Files**: Sample CSV, JSON, XML files (included in project)
- **Database**: SQLite database created locally

## Ethical Considerations

- All websites scraped are either:
  - Publicly available practice sites designed for scraping
  - Sites that explicitly allow scraping in their terms of service
- Rate limiting implemented (2+ seconds between requests)
- robots.txt checked before scraping
- Proper User-Agent headers used
- No copyrighted or restricted content extracted

## Common Issues and Solutions

### Issue: 403 Forbidden Error
**Solution**: Add proper headers to your requests:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Educational Purpose)'
}
response = requests.get(url, headers=headers)
```

### Issue: Timeout Errors
**Solution**: Increase timeout or check internet connection:
```python
response = requests.get(url, timeout=30)
```

### Issue: Missing Elements in HTML
**Solution**: Website structure may have changed. Verify selectors using browser developer tools.

### Issue: Selenium WebDriver Error
**Solution**: Make sure ChromeDriver/GeckoDriver is installed and in PATH, or specify the path:
```python
from selenium.webdriver.chrome.service import Service
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)
```

## Notes

- Always check a website's robots.txt and terms of service before scraping
- Use APIs when available instead of scraping
- Implement rate limiting to be respectful to servers
- Save extracted data regularly to avoid re-scraping
- Handle errors gracefully (network errors, missing elements, etc.)

## References

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://requests.readthedocs.io/)
- [Web Scraping Ethics](https://www.scrapehero.com/web-scraping-ethics/)

