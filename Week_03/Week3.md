## Week 3 Tasks — Data Preparation, EDA, and Intro Modeling (R)

Week 3 mirrors Week 2’s workflow, but your submission must be in R Markdown. Choose a dataset you find interesting (or reuse the Week 2 dataset). Focus on a clean, reproducible analysis that runs top‑to‑bottom.

Reference dataset (optional): [Uber Data Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)

Guidance:
- Prefer tidy/tabular data. Perform light cleaning before EDA if needed.
- Keep code reproducible; avoid manual steps.

---

### Task 1 — Load Data and Inspect
- Load the dataset and show the first 5–10 rows and shape/dimensions.
- Briefly describe the purpose of the dataset and key variables.

---

### Task 2 — Data Types, Summary Stats, and Missingness
- Check and correct data types.
- Provide summary statistics for numeric/categorical columns.
- Report missing value counts and percentages per column.

---

### Task 3 — Data Cleaning
- Handle missing values and duplicates.
- Standardize column names and fix inconsistent categorical labels.
- Briefly document cleaning decisions.

---

### Task 4 — Exploratory Data Analysis (EDA)
- Explore distributions of key variables and relationships among them.
- Write 3–5 short observations.

---

### Task 5 — Data Visualization
- Create at least 2 plots with clear captions.

---

### Task 6 — Class Imbalance (if applicable)
- If classification target exists, assess class proportions and apply one strategy if imbalance exists.

---

### Task 7 — Feature Engineering
- Create/transform at least 2 features useful for modeling; drop irrelevant columns if needed.

---

### Task 8 — Baseline Modeling
- Train a simple baseline model suitable for your problem (classification or regression). Show training code and predictions.

---

### Task 9 — Evaluation
- Use appropriate metrics and provide a short interpretation (2–4 sentences).

---

### Task 10 — Findings and Next Steps
- Summarize 3–5 insights and propose 2 next steps to improve the analysis/model.

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add brief comments for complex operations
- Ensure the Rmd document knits to PDF without errors
- Use consistent formatting and follow R style conventions (tidyverse style guide)
- Load all required libraries in the setup chunk at the beginning

**Data Analysis:**
- Choose appropriate visualizations for your data types and research questions
- Use ggplot2 for all plots with clear titles, axis labels, and themes
- Provide 2-3 sentence interpretations under each visualization
- Justify your data cleaning decisions with brief explanations

**Modeling:**
- Use appropriate train/test splits (typically 80/20) with set.seed() for reproducibility
- Select baseline models suitable for your problem type (glm for classification/regression)
- Report multiple relevant metrics and interpret what they mean for your specific dataset
- Handle class imbalance if present (use stratified splits, class weights, or resampling)

**Documentation:**
- Write clear markdown sections explaining your approach for each major task
- Include brief dataset description and any assumptions you make
- Document any data quality issues you discover and how you address them
- Provide actionable insights and concrete next steps in your final summary

**R Markdown Best Practices:**
- Use meaningful chunk names (e.g., `{r load-data}` instead of `{r}`)
- Set `echo = TRUE` for code you want to show, `echo = FALSE` for setup/loading
- Use `include = FALSE` for chunks that prepare data but don't need to appear in output
- Ensure all plots render correctly in PDF format

### Deliverables

Submit an R Markdown document only (template provided in `Week_03/submission_template/`):

- `Week3_Tasks.Rmd` (knit to PDF)

Your submission must include solutions to all tasks, with runnable code and brief annotations under plots and results.