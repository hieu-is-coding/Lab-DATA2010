"""
Task 4: File Format Extraction
This script demonstrates how to extract data from different file formats: CSV, JSON, XML, and PDF.
"""

import pandas as pd
import json
import xml.etree.ElementTree as ET
from PyPDF2 import PdfReader
import os

# 1. Extract from CSV
print("=== CSV Extraction ===")
if os.path.exists('data.csv'):
    df_csv = pd.read_csv('data.csv')
    print(f"CSV file loaded: {len(df_csv)} rows")
    print(df_csv.head())
else:
    # Create sample CSV for demonstration
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 28]}
    df_csv = pd.DataFrame(data)
    df_csv.to_csv('data.csv', index=False)
    print("Created sample data.csv")
    print(df_csv)

# 2. Extract from JSON
print("\n=== JSON Extraction ===")
if os.path.exists('data.json'):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    df_json = pd.DataFrame(json_data)
    print(f"JSON file loaded: {len(df_json)} records")
    print(df_json)
else:
    print("data.json not found. Please create it first.")

# 3. Extract from XML
print("\n=== XML Extraction ===")
if os.path.exists('data.xml'):
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    xml_data = []
    for item in root.findall('item'):
        xml_data.append({
            'name': item.find('name').text,
            'value': item.find('value').text
        })
    df_xml = pd.DataFrame(xml_data)
    print(f"XML file loaded: {len(df_xml)} items")
    print(df_xml)
else:
    print("data.xml not found. Please create it first.")

# 4. Extract text from PDF (basic)
print("\n=== PDF Text Extraction ===")
pdf_file = 'sample.pdf'  # Change to your PDF file name
if os.path.exists(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        num_pages = min(3, len(reader.pages))  # First 3 pages or all if less
        
        for i in range(num_pages):
            page = reader.pages[i]
            text += page.extract_text()
        
        print(f"Extracted {len(text)} characters from {num_pages} page(s)")
        print("\nFirst 500 characters:")
        print(text[:500])
        
        # Save extracted text
        with open('extracted_text.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("\nExtracted text saved to extracted_text.txt")
    except Exception as e:
        print(f"PDF extraction error: {e}")
        print("Note: PDF extraction may not work perfectly for all PDF formats")
else:
    print(f"{pdf_file} not found. Skipping PDF extraction.")
    print("Note: To test PDF extraction, add a PDF file named 'sample.pdf'")

print("\n=== Summary ===")
print("File extraction completed!")
print("- CSV: ✓" if os.path.exists('data.csv') else "- CSV: ✗")
print("- JSON: ✓" if os.path.exists('data.json') else "- JSON: ✗")
print("- XML: ✓" if os.path.exists('data.xml') else "- XML: ✗")
print("- PDF: ✓" if os.path.exists(pdf_file) else "- PDF: ✗ (optional)")

