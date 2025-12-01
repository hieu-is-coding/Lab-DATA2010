"""
Task 5: Database Extraction
This script demonstrates how to create a SQLite database and extract data from it.
"""

import sqlite3
import pandas as pd
import os

# Step 1: Create database and table (if not exists)
print("=== Creating Database ===")
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        salary REAL
    )
''')

# Check if table is empty, if so insert sample data
cursor.execute('SELECT COUNT(*) FROM employees')
count = cursor.fetchone()[0]

if count == 0:
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
    print("Sample data inserted into employees table")
else:
    print(f"Table already contains {count} records")

conn.close()

# Step 2: Extract data from database
print("\n=== Extracting Data from Database ===")
conn = sqlite3.connect('sample.db')

# Method 1: Using pandas read_sql
print("\n1. Employees with salary > 65000:")
query = "SELECT * FROM employees WHERE salary > 65000"
df = pd.read_sql(query, conn)
print(df)

# Method 2: Using cursor for aggregation
print("\n2. Average salary by department:")
cursor = conn.cursor()
cursor.execute("SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department")
results = cursor.fetchall()
for row in results:
    print(f"  {row[0]}: ${row[1]:.2f}")

# Method 3: Extract all data
print("\n3. All employees:")
df_all = pd.read_sql("SELECT * FROM employees", conn)
print(df_all)

# Save to CSV
df_all.to_csv('employees.csv', index=False)
print(f"\nExtracted {len(df_all)} records to employees.csv")

conn.close()
print("\nDatabase operations completed!")

