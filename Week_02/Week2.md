## Week 2 Tasks — Data Preparation, EDA, and Intro Modeling

Choose a dataset you find interesting (or use the reference Uber dataset below). This week focuses on a practical, end‑to‑end data science workflow: load data, understand structure and quality, clean/engineer features, explore visually, build a simple baseline model, and evaluate it.

Reference dataset (optional): [Uber Data Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)

Guidance:
- Prefer tidy/tabular data (CSV/Parquet). If multiple files exist, start with the main fact table.
- If necessary, perform light cleaning (parse dates, fix column names, handle missing values) before EDA.
- Keep your work reproducible: the document should run top‑to‑bottom with no manual steps.

---

### Task 1 — Load Data and Inspect
- Load the dataset from local path or via Kaggle API.
- Show the first 5–10 rows and dataset shape.
- Briefly describe the purpose of the dataset and key variables.

---

### Task 2 — Data Types, Summary Stats, and Missingness
- List each column’s data type and correct any obvious mis‑types (e.g., strings parsed as dates, categories).
- Provide summary statistics for numeric and categorical columns.
- Report missing value counts and percentages per column.

---

### Task 3 — Data Cleaning
- Handle missing values (drop, impute, or flag) and remove clear duplicates.
- Standardize column names (snake_case) and fix inconsistent categorical labels if present.
- Document each cleaning decision in brief bullet points.

---

### Task 4 — Exploratory Data Analysis (EDA)
- Explore distributions of key variables and detect outliers.
- Examine relationships among important variables to generate hypotheses.
- Write 3–5 short observations from EDA.

---

### Task 5 — Data Visualization
- Create at least 2 clear plots highlighting interesting patterns.
- Add captions beneath each plot with the key takeaway.

---

### Task 6 — Class Imbalance (if applicable)
- If you have a classification target, check class proportions.
- Apply one strategy if imbalance exists (e.g., class weights, resampling) and justify briefly.

---

### Task 7 — Feature Engineering
- Create or transform at least 2 features that could help a model (e.g., one‑hot encoding, date parts, text length, binning).
- Drop/leakage‑prone or irrelevant columns where appropriate.

---

### Task 8 — Baseline Modeling
- Train a simple baseline model (e.g., LogisticRegression/RandomForest for classification; LinearRegression/RandomForest for regression).
- Split data into train/test (or use cross‑validation). Show basic training code and predictions.

---

### Task 9 — Evaluation
- Use appropriate metrics (e.g., accuracy/F1/AUROC for classification; RMSE/MAE/R^2 for regression).
- Provide a compact results table/printout and a 2–4 sentence interpretation.

---

### Task 10 — Findings and Next Steps
- Summarize 3–5 insights from EDA and modeling.
- Propose 2 concrete next steps to improve the model or analysis.

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add brief comments for complex operations
- Ensure all code cells run without errors when executed sequentially
- Use consistent formatting and follow Python style conventions (PEP 8)
- Import all required libraries at the beginning of the notebook

**Data Analysis:**
- Choose appropriate visualizations for your data types and research questions
- Include clear titles, axis labels, and legends for all plots
- Provide 2-3 sentence interpretations under each visualization
- Justify your data cleaning decisions with brief explanations

**Modeling:**
- Use appropriate train/test splits (typically 80/20) with random seeds for reproducibility
- Select baseline models suitable for your problem type (classification vs regression)
- Report multiple relevant metrics and interpret what they mean for your specific dataset
- Handle class imbalance if present (use stratified splits, class weights, or resampling)

**Documentation:**
- Write clear markdown cells explaining your approach for each major task
- Include brief dataset description and any assumptions you make
- Document any data quality issues you discover and how you address them
- Provide actionable insights and concrete next steps in your final summary

### Deliverables

Submit a Jupyter Notebook only (template provided in `Week_02/submission_template/`):

- `Week2_Tasks.ipynb`

Your submission must include solutions to all tasks, with runnable code and brief annotations under plots and results.
