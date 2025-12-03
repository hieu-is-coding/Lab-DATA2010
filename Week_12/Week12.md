## Week 12 Tasks — Data Extraction

This week focuses on data extraction techniques, which are fundamental skills for data scientists. You'll learn how to extract data from various sources including websites, APIs, files, and databases. Data extraction is often the first step in any data science project, and mastering these techniques will enable you to work with diverse data sources.

### What is Data Extraction?

Data extraction is the process of retrieving data from various sources and converting it into a format suitable for analysis. In this lab, you'll explore:

- **Web Scraping**: Extracting data from HTML web pages
- **API Extraction**: Retrieving data from REST APIs
- **File Parsing**: Extracting data from CSV, JSON, XML, and PDF files
- **Database Queries**: Extracting data from SQL databases
- **Text Extraction**: Parsing structured and unstructured text data

### Prerequisites

1. **Python Libraries** (install if needed):
   ```bash
   pip install requests beautifulsoup4 lxml pandas openpyxl PyPDF2 python-docx
   ```

2. **For API tasks**: You may need API keys for some services (we'll use free/public APIs)

3. **For database tasks**: SQLite (comes with Python) or access to a database

### Submission Format

**Important**: You must submit **TWO separate files**:
1. **PDF Report** (`Week12_Report.pdf`) - Contains all tasks with screenshots, code outputs, and explanations
2. **Source Code Zip** (`Week12_SourceCode.zip`) - Contains all your Python scripts and notebooks

See the "Deliverables" section at the end for detailed requirements.

---

### Task 1 — Web Scraping Basics: Extracting Data from HTML

Learn to extract structured data from HTML web pages using BeautifulSoup.

**Steps:**

1. **Create a simple HTML file** (`sample.html`) for practice:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Sample Data</title>
   </head>
   <body>
       <h1>Student Information</h1>
       <table>
           <tr>
               <th>Name</th>
               <th>Age</th>
               <th>Grade</th>
           </tr>
           <tr>
               <td>Alice</td>
               <td>20</td>
               <td>A</td>
           </tr>
           <tr>
               <td>Bob</td>
               <td>21</td>
               <td>B</td>
           </tr>
           <tr>
               <td>Charlie</td>
               <td>19</td>
               <td>A</td>
           </tr>
       </table>
   </body>
   </html>
   ```

2. **Create a Python script** (`web_scrape_basic.py`):
   ```python
   from bs4 import BeautifulSoup
   import pandas as pd
   
   # Read HTML file
   with open('sample.html', 'r', encoding='utf-8') as file:
       html_content = file.read()
   
   # Parse HTML
   soup = BeautifulSoup(html_content, 'html.parser')
   
   # Extract table data
   table = soup.find('table')
   rows = table.find_all('tr')
   
   # Extract headers
   headers = [th.text.strip() for th in rows[0].find_all('th')]
   
   # Extract data rows
   data = []
   for row in rows[1:]:
       cells = row.find_all('td')
       data.append([cell.text.strip() for cell in cells])
   
   # Create DataFrame
   df = pd.DataFrame(data, columns=headers)
   print(df)
   ```

3. **Run the script** and verify the output.

**Deliverable**: 
- Your `sample.html` file
- Your `web_scrape_basic.py` script
- Screenshot of the output showing the extracted DataFrame

---

### Task 2 — Web Scraping from Live Websites

Extract data from a real website (use a website that allows scraping or a public data source).

**Important**: Always check a website's `robots.txt` and terms of service before scraping. For this task, use a website that explicitly allows scraping or use a practice site.

**Steps:**

1. **Choose a target website** (suggestions):
   - [Quotes to Scrape](http://quotes.toscrape.com/) - Practice site designed for scraping
   - [Books to Scrape](http://books.toscrape.com/) - Another practice site
   - Or use a public data website that allows scraping

2. **Create a script** (`web_scrape_live.py`) to extract quotes:
   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd
   
   # URL of the website
   url = 'http://quotes.toscrape.com/'
   
   # Send GET request
   response = requests.get(url)
   
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
       print(df.head(10))
       
       # Save to CSV
       df.to_csv('quotes.csv', index=False)
       print(f"\nExtracted {len(df)} quotes and saved to quotes.csv")
   else:
       print(f"Failed to retrieve page. Status code: {response.status_code}")
   ```

3. **Handle pagination** (if applicable):
   ```python
   # Extract from multiple pages
   base_url = 'http://quotes.toscrape.com/page/'
   all_quotes = []
   
   for page in range(1, 6):  # First 5 pages
       url = f'{base_url}{page}/'
       response = requests.get(url)
       # ... (extraction code)
   ```

**Deliverable**: 
- Your `web_scrape_live.py` script
- Screenshot showing extracted data
- The `quotes.csv` file (or similar output file)

---

### Task 3 — API Data Extraction

Extract data from REST APIs using the `requests` library.

**Steps:**

1. **Use a free public API** (no key required):
   - [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake REST API for testing
   - [REST Countries](https://restcountries.com/) - Country information
   - [OpenWeatherMap](https://openweathermap.org/api) - Weather data (requires free API key)

2. **Create a script** (`api_extract.py`) to extract data:
   ```python
   import requests
   import pandas as pd
   import json
   
   # Example 1: JSONPlaceholder API
   url = 'https://jsonplaceholder.typicode.com/posts'
   response = requests.get(url)
   
   if response.status_code == 200:
       data = response.json()
       df = pd.DataFrame(data)
       print(f"Extracted {len(df)} posts")
       print(df.head())
       df.to_csv('posts.csv', index=False)
   else:
       print(f"Error: {response.status_code}")
   
   # Example 2: REST Countries API
   url = 'https://restcountries.com/v3.1/all?fields=name
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
       print(df_countries)
       df_countries.to_csv('countries.csv', index=False)
   ```

3. **Handle API with authentication** (if using an API that requires a key):
   ```python
   # Example with API key (replace with your actual key)
   api_key = 'your_api_key_here'
   url = f'https://api.example.com/data?api_key={api_key}'
   response = requests.get(url)
   ```

**Deliverable**: 
- Your `api_extract.py` script
- Screenshot showing extracted data from at least 2 different APIs
- CSV files with extracted data

---

### Task 4 — File Format Extraction

Extract data from different file formats: CSV, JSON, XML, and PDF.

**Steps:**

1. **Create sample files** for practice:
   - `data.csv` (already familiar)
   - `data.json`
   - `data.xml`
   - `sample.pdf` (optional, can use an existing PDF)

2. **Create a script** (`file_extract.py`):
   ```python
   import pandas as pd
   import json
   import xml.etree.ElementTree as ET
   from PyPDF2 import PdfReader
   
   # 1. Extract from CSV
   print("=== CSV Extraction ===")
   df_csv = pd.read_csv('data.csv')
   print(df_csv.head())
   
   # 2. Extract from JSON
   print("\n=== JSON Extraction ===")
   with open('data.json', 'r') as file:
       json_data = json.load(file)
   df_json = pd.DataFrame(json_data)
   print(df_json.head())
   
   # 3. Extract from XML
   print("\n=== XML Extraction ===")
   tree = ET.parse('data.xml')
   root = tree.getroot()
   
   xml_data = []
   for item in root.findall('item'):
       xml_data.append({
           'name': item.find('name').text,
           'value': item.find('value').text
       })
   df_xml = pd.DataFrame(xml_data)
   print(df_xml)
   
   # 4. Extract text from PDF (basic)
   print("\n=== PDF Text Extraction ===")
   try:
       reader = PdfReader('sample.pdf')
       text = ""
       for page in reader.pages[:3]:  # First 3 pages
           text += page.extract_text()
       print(f"Extracted {len(text)} characters from PDF")
       print(text[:500])  # First 500 characters
   except Exception as e:
       print(f"PDF extraction error: {e}")
   ```

3. **Create sample JSON file** (`data.json`):
   ```json
   [
       {"name": "Alice", "age": 25, "city": "New York"},
       {"name": "Bob", "age": 30, "city": "London"},
       {"name": "Charlie", "age": 28, "city": "Tokyo"}
   ]
   ```

4. **Create sample XML file** (`data.xml`):
   ```xml
   <?xml version="1.0"?>
   <root>
       <item>
           <name>Product A</name>
           <value>100</value>
       </item>
       <item>
           <name>Product B</name>
           <value>200</value>
       </item>
       <item>
           <name>Product C</name>
           <value>150</value>
       </item>
   </root>
   ```

**Deliverable**: 
- Your `file_extract.py` script
- Sample data files (JSON, XML)
- Screenshots showing extraction from each file format

---

### Task 5 — Database Extraction

Extract data from a SQL database using Python.

**Steps:**

1. **Create a SQLite database** with sample data:
   ```python
   import sqlite3
   import pandas as pd
   
   # Create database and table
   conn = sqlite3.connect('sample.db')
   cursor = conn.cursor()
   
   # Create table
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS employees (
           id INTEGER PRIMARY KEY,
           name TEXT,
           department TEXT,
           salary REAL
       )
   ''')
   
   # Insert sample data
   employees = [
       ('Alice', 'Engineering', 75000),
       ('Bob', 'Marketing', 65000),
       ('Charlie', 'Engineering', 80000),
       ('David', 'Sales', 60000),
       ('Emma', 'Marketing', 70000)
   ]
   
   cursor.executemany('INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)', employees)
   conn.commit()
   conn.close()
   print("Database created successfully!")
   ```

2. **Extract data from the database**:
   ```python
   import sqlite3
   import pandas as pd
   
   # Connect to database
   conn = sqlite3.connect('sample.db')
   
   # Method 1: Using pandas read_sql
   query = "SELECT * FROM employees WHERE salary > 65000"
   df = pd.read_sql(query, conn)
   print("Employees with salary > 65000:")
   print(df)
   
   # Method 2: Using cursor
   cursor = conn.cursor()
   cursor.execute("SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department")
   results = cursor.fetchall()
   print("\nAverage salary by department:")
   for row in results:
       print(f"{row[0]}: ${row[1]:.2f}")
   
   # Method 3: Extract all data
   df_all = pd.read_sql("SELECT * FROM employees", conn)
   df_all.to_csv('employees.csv', index=False)
   print(f"\nExtracted {len(df_all)} records to employees.csv")
   
   conn.close()
   ```

**Deliverable**: 
- Your database creation script
- Your database extraction script
- Screenshot showing extracted data
- The `employees.csv` file

---

### Task 6 — Advanced Web Scraping: Handling Dynamic Content

Some websites load content dynamically using JavaScript. Learn to handle such cases.

**Steps:**

1. **Identify if a site uses JavaScript**:
   - If content doesn't appear in the HTML source but shows in browser, it's likely JavaScript-rendered
   - Use browser developer tools to inspect network requests

2. **Option A: Use Selenium** (for JavaScript-heavy sites):
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   import pandas as pd
   
   # Note: Requires ChromeDriver or GeckoDriver
   # Install: pip install selenium
   
   # Setup (you may need to adjust driver path)
   driver = webdriver.Chrome()  # or Firefox()
   
   try:
       url = 'https://example-dynamic-site.com'
       driver.get(url)
       
       # Wait for content to load
       wait = WebDriverWait(driver, 10)
       element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
       
       # Extract data
       items = driver.find_elements(By.CLASS_NAME, "item")
       data = []
       for item in items:
           data.append({
               'text': item.text,
               # Extract other attributes
           })
       
       df = pd.DataFrame(data)
       print(df)
       
   finally:
       driver.quit()
   ```

3. **Option B: Use requests with API endpoints** (preferred if possible):
   - Many dynamic sites load data via API calls
   - Use browser developer tools → Network tab to find API endpoints
   - Extract data directly from the API (faster and more reliable)

**Deliverable**: 
- Your script for handling dynamic content (or explanation of why Selenium wasn't needed)
- Screenshot showing extracted data
- Brief explanation of the approach used

---

### Task 7 — Data Extraction Pipeline

Create a complete data extraction pipeline that combines multiple sources.

**Steps:**

1. **Create a pipeline script** (`extraction_pipeline.py`):
   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd
   import sqlite3
   import json
   from datetime import datetime
   
   def extract_from_api():
       """Extract data from an API"""
       url = 'https://jsonplaceholder.typicode.com/users'
       response = requests.get(url)
       if response.status_code == 200:
           return pd.DataFrame(response.json())
       return pd.DataFrame()
   
   def extract_from_html():
       """Extract data from HTML file"""
       with open('sample.html', 'r') as file:
           html = file.read()
       soup = BeautifulSoup(html, 'html.parser')
       # ... extraction logic
       return pd.DataFrame()  # Placeholder
   
   def extract_from_database():
       """Extract data from database"""
       conn = sqlite3.connect('sample.db')
       df = pd.read_sql("SELECT * FROM employees", conn)
       conn.close()
       return df
   
   def combine_dataframes(df_list):
       """Combine multiple dataframes"""
       # This is a simple example - adjust based on your needs
       combined = pd.concat(df_list, ignore_index=True)
       return combined
   
   # Main pipeline
   print("Starting data extraction pipeline...")
   
   # Extract from multiple sources
   api_data = extract_from_api()
   db_data = extract_from_database()
   
   # Combine and save
   all_data = [api_data, db_data]
   combined_df = combine_dataframes(all_data)
   
   # Save results
   timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
   output_file = f'extracted_data_{timestamp}.csv'
   combined_df.to_csv(output_file, index=False)
   
   print(f"Pipeline completed! Data saved to {output_file}")
   print(f"Total records: {len(combined_df)}")
   ```

2. **Add error handling and logging**:
   ```python
   import logging
   
   logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
   
   try:
       # Your extraction code
       logging.info("Extraction successful")
   except Exception as e:
       logging.error(f"Extraction failed: {e}")
   ```

**Deliverable**: 
- Your `extraction_pipeline.py` script
- Screenshot showing the pipeline execution
- Output file(s) generated by the pipeline

---

### Task 8 — Ethical Web Scraping and Best Practices

Demonstrate understanding of ethical scraping practices and implement rate limiting.

**Steps:**

1. **Implement rate limiting** to avoid overwhelming servers:
   ```python
   import requests
   import time
   from bs4 import BeautifulSoup
   
   def scrape_with_delay(url, delay=1):
       """Scrape with a delay between requests"""
       time.sleep(delay)  # Be respectful to the server
       response = requests.get(url)
       return response
   
   # Example: Scrape multiple pages with delay
   base_url = 'http://quotes.toscrape.com/page/'
   for page in range(1, 6):
       url = f'{base_url}{page}/'
       response = scrape_with_delay(url, delay=2)  # 2 second delay
       # Process response
       print(f"Scraped page {page}")
   ```

2. **Check robots.txt**:
   ```python
   import requests
   from urllib.robotparser import RobotFileParser
   
   def check_robots_txt(base_url, path):
       """Check if a path is allowed by robots.txt"""
       rp = RobotFileParser()
       rp.set_url(f"{base_url}/robots.txt")
       rp.read()
       return rp.can_fetch('*', path)
   
   # Example
   base_url = 'https://example.com'
   path = '/data'
   if check_robots_txt(base_url, path):
       print("Scraping is allowed")
   else:
       print("Scraping is not allowed")
   ```

3. **Use proper headers**:
   ```python
   headers = {
       'User-Agent': 'Mozilla/5.0 (Educational Purpose - Data Science Lab)',
       'Accept': 'text/html,application/xhtml+xml',
   }
   response = requests.get(url, headers=headers)
   ```

**Deliverable**: 
- Your script demonstrating ethical scraping practices
- Brief explanation (2-3 sentences) of why these practices are important
- Screenshot showing rate-limited scraping

---

### Guidelines

**Getting Help:**
- If a website blocks your requests, try adding proper headers
- Some websites require cookies or sessions - use `requests.Session()`
- Check if the website has an official API before scraping
- Always respect robots.txt and terms of service

**Best Practices:**
- **Always check robots.txt** before scraping
- **Use rate limiting** to avoid overwhelming servers
- **Respect terms of service** of websites
- **Use APIs when available** instead of scraping
- **Handle errors gracefully** (network errors, missing elements, etc.)
- **Save extracted data** regularly to avoid re-scraping
- **Use proper headers** to identify your scraper
- **Be mindful of copyright** and data usage rights

**Common Issues:**
- **403 Forbidden**: Website is blocking your requests - try adding headers or using a different approach
- **Timeout errors**: Increase timeout or check your internet connection
- **Missing elements**: Website structure may have changed - verify selectors
- **Rate limiting**: Implement delays between requests
- **JavaScript content**: Use Selenium or find the API endpoint

**Error Handling:**
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises exception for bad status codes
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    # Handle error appropriately
```

---

### Deliverables

You need to submit **TWO files**:

#### 1. PDF Report (`Week12_Report.pdf`)

A comprehensive PDF document containing:

- **Cover page** with your name, student ID, and date
- **For each task (Tasks 1-8)**:
  - Task number and title
  - Brief description of what you did
  - Screenshots showing:
    - Code execution
    - Output/results
    - Extracted data samples
  - Brief explanation (2-3 sentences) of the extraction method used
  - Any challenges encountered and how you solved them
  
- **Required Screenshots**:
  - Task 1: HTML parsing output showing extracted table data
  - Task 2: Live website scraping with extracted quotes/data
  - Task 3: API extraction showing data from at least 2 different APIs
  - Task 4: File extraction from CSV, JSON, XML (and PDF if attempted)
  - Task 5: Database extraction showing SQL queries and results
  - Task 6: Dynamic content handling (or explanation of approach)
  - Task 7: Pipeline execution showing combined data extraction
  - Task 8: Ethical scraping practices demonstration

- **Summary/Reflection** (2-3 paragraphs):
  - What you learned about data extraction
  - Comparison of different extraction methods (web scraping vs. APIs vs. databases)
  - Ethical considerations in data extraction
  - Challenges faced and how you overcame them
  - How these skills apply to real-world data science projects

**PDF Format Guidelines:**
- Use clear headings for each task
- Ensure screenshots are readable and properly labeled
- Keep the document well-organized and professional
- Maximum 25 pages (typically 15-20 pages is sufficient)

#### 2. Source Code Zip File (`Week12_SourceCode.zip`)

A zip file containing all your source code and project files:

```
Week12_SourceCode/
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
├── sample.db                     # SQLite database (if created)
├── quotes.csv                    # Example extracted data
├── employees.csv                 # Example extracted data
├── requirements.txt              # Python dependencies
└── README.md                     # Brief documentation
```

**README.md should include:**
- Project description
- Installation instructions: `pip install -r requirements.txt`
- How to run each script
- Data sources used
- Any special instructions or notes
- Ethical considerations and permissions obtained

**requirements.txt should include:**
```
requests>=2.28.0
beautifulsoup4>=4.11.0
lxml>=4.9.0
pandas>=1.5.0
openpyxl>=3.0.0
PyPDF2>=3.0.0
selenium>=4.0.0  # Optional, for Task 6
```

**Important Notes:**
- Make sure all code files are included and complete
- Test that your code works before submitting
- The zip file should extract to a single folder (not multiple files at root level)
- Do NOT include the PDF report in the zip file (submit separately)
- Include sample data files if they're small and necessary for demonstration
- For large extracted datasets, include a sample (first 10-20 rows) instead of the full dataset

---

### Additional Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML parsing guide
- [Requests Library Documentation](https://requests.readthedocs.io/) - HTTP library for Python
- [Web Scraping with Python](https://realpython.com/python-web-scraping-practical-introduction/) - Comprehensive tutorial
- [API Best Practices](https://restfulapi.net/) - REST API guidelines
- [SQLite Python Tutorial](https://docs.python.org/3/library/sqlite3.html) - Database operations
- [Ethical Web Scraping Guide](https://www.scrapehero.com/web-scraping-ethics/) - Best practices

---

### Submission Checklist

**Tasks Completed:**
- [ ] Task 1: HTML scraping from local file works
- [ ] Task 2: Live website scraping extracts data successfully
- [ ] Task 3: API extraction from at least 2 different APIs
- [ ] Task 4: File extraction from CSV, JSON, XML (and PDF if attempted)
- [ ] Task 5: Database creation and extraction works
- [ ] Task 6: Dynamic content handling (or explanation provided)
- [ ] Task 7: Data extraction pipeline combines multiple sources
- [ ] Task 8: Ethical scraping practices demonstrated

**PDF Report:**
- [ ] Cover page with name, student ID, and date
- [ ] All 8 tasks documented with screenshots
- [ ] Screenshots are clear and readable
- [ ] Each task has brief explanation
- [ ] Summary/reflection section included
- [ ] PDF is properly formatted and professional

**Source Code Zip:**
- [ ] All Python scripts included (8+ scripts)
- [ ] Sample data files included (HTML, JSON, XML)
- [ ] requirements.txt included with all dependencies
- [ ] README.md with clear instructions
- [ ] Zip file extracts to a single folder
- [ ] All code tested and working
- [ ] Ethical considerations documented

**Final Check:**
- [ ] PDF report submitted separately (not in zip)
- [ ] Source code zip file submitted separately
- [ ] Both files named correctly (Week12_Report.pdf and Week12_SourceCode.zip)
- [ ] All websites/APIs used are publicly accessible or permission obtained
- [ ] Rate limiting implemented where appropriate

---

**Remember**: Data extraction is a powerful skill, but it comes with responsibilities. Always respect website terms of service, implement rate limiting, and use APIs when available. The goal is to learn extraction techniques while being ethical and respectful to data sources.

