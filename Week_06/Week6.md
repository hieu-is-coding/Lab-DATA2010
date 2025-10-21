## Week 6 Tasks — Introduction to Data Wrangling in R and Python

Using a dataset of your choice (or the provided sample datasets), demonstrate essential data wrangling skills including data loading, cleaning, transformation, and aggregation. You may complete the tasks in either R (tidyverse) or Python (pandas). If you submit both R and Python solutions, you will receive 2 bonus points.

Reference datasets (choose one or use your own):
- [Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file) - Classic dataset for data science practice
- [Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data) - E-commerce sales data
- [Customer Data](https://www.kaggle.com/datasets/parulpandey/customer-segmentation) - Customer segmentation data
- [Weather Data](https://www.kaggle.com/datasets/muthuj7/weather-dataset) - Weather measurements over time

Guidance: Choose a dataset that has some data quality issues (missing values, inconsistent formats, etc.) to make the wrangling tasks meaningful.

### Task 1 — Data Loading and Initial Exploration
- Load your chosen dataset and display basic information (shape, column names, data types)
- Show the first 10 rows and last 5 rows
- Generate summary statistics for numeric columns
- Identify potential data quality issues (missing values, outliers, inconsistent formats)

---

### Task 2 — Data Cleaning and Preprocessing
- Handle missing values using appropriate strategies (drop, impute, or flag)
- Clean and standardize text data (remove extra spaces, convert case, etc.)
- Fix data type issues (convert strings to dates, numeric strings to numbers)
- Remove or handle duplicate records
- Create a data quality report showing before/after cleaning

---

### Task 3 — Data Transformation and Feature Engineering
- Create new derived variables from existing ones (e.g., age groups, categories)
- Apply mathematical transformations (log, square root, etc.) where appropriate
- Encode categorical variables (one-hot encoding, label encoding)
- Create time-based features if applicable (day of week, month, season)
- Demonstrate at least 3 different transformation techniques

---

### Task 4 — Data Aggregation and Grouping Operations
- Perform groupby operations with multiple aggregation functions
- Create pivot tables or cross-tabulations
- Calculate summary statistics by groups
- Merge/join multiple datasets if available
- Create a final cleaned and transformed dataset ready for analysis

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add comments for complex operations
- Ensure both Rmd and Jupyter notebook run top-to-bottom without errors
- Use consistent formatting and follow language-specific style conventions
- Load all required libraries at the beginning of each document

**Data Wrangling Best Practices:**
- Document your data cleaning decisions and reasoning
- Preserve original data when possible (create copies before transformations)
- Use appropriate data types to optimize memory usage
- Handle edge cases and potential errors gracefully
- Create reproducible data processing pipelines

**R Best Practices (for R submission):**
- Use tidyverse functions (dplyr, tidyr, readr, lubridate)
- Use meaningful chunk names (e.g., `{r data-loading}`)
- Set `echo = TRUE` for code you want to show, `echo = FALSE` for setup
- Use `include = FALSE` for chunks that prepare data but don't need to appear
- Ensure all operations render correctly in PDF format

**Python Best Practices (for Python submission):**
- Use pandas for data manipulation and numpy for numerical operations
- Use markdown cells to explain your data wrangling approach
- Keep code cells focused and well-commented
- Use appropriate pandas methods (avoid loops when possible)
- Ensure data processing is efficient and memory-conscious

**Documentation Requirements:**
- Explain your data cleaning strategy for each step
- Document any assumptions made about the data
- Provide before/after comparisons for major transformations
- Include data quality metrics and validation checks
- Explain the business logic behind feature engineering decisions

### Deliverables

Choosing R or Python to submit:

- **R**: An R Markdown file `Week6_Tasks.Rmd` and `Week6_Tasks.pdf` (knitted to PDF) (10 points)
- **Python**: A Jupyter Notebook `Week6_Tasks.ipynb` (10 points)
- **Bonus**: Submit both R and Python solutions for 2 bonus points

Use the provided templates in `Week_06/submission_template/`.

Your submission should include all tasks, documented data cleaning decisions, and a final processed dataset ready for analysis.

---

### Evaluation Criteria

**Data Loading (25%):**
- Proper data import and initial exploration
- Identification of data quality issues
- Clear documentation of dataset characteristics

**Data Cleaning (30%):**
- Appropriate handling of missing values
- Effective text and data type cleaning
- Removal of duplicates and outliers
- Data quality improvement metrics

**Data Transformation (25%):**
- Creative and appropriate feature engineering
- Proper encoding of categorical variables
- Mathematical transformations where relevant
- Clear documentation of transformation logic

**Data Aggregation (20%):**
- Effective use of grouping and aggregation
- Meaningful summary statistics
- Proper data merging/joining if applicable
- Final dataset ready for analysis

**Code Quality and Documentation:**
- Clean, readable, and well-commented code
- Proper use of language-specific best practices
- Comprehensive documentation of decisions
- Reproducible data processing pipeline
