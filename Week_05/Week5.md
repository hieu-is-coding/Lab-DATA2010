## Week 5 Tasks — Data Visualization in R and Python

Using a dataset you find interesting (or the example Uber dataset linked below), create a concise but insightful data visualization report. Focus on effective chart selection, clear aesthetics, and telling a data story. You may complete the tasks in either R (ggplot2) or Python (seaborn/matplotlib). Templates are provided in `Week_05/submission_template`.

Reference dataset (optional): 
- [Uber Data Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)
- [Earthquake stunami risk](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset/data)
- [International Airport Flights](https://www.kaggle.com/datasets/mohammedalsubaie/king-khalid-international-airport-flights-dataset)

Guidance: Prefer tidy/tabular data; if your dataset needs light cleaning (rename columns, parse dates), do that in the notebook/Rmd before plotting.

### Task 1 — Setup and Data Loading
- Load the dataset and show first 5–10 rows
- Briefly describe variables and expected data types

---

### Task 2 — Univariate Visualizations
- Create at least 2 plots for single variables (e.g., histogram/density for numeric; bar plot for categorical)
- Annotate the key takeaway under each plot

---

### Task 3 — Bivariate Visualizations
- Create at least 2 plots showing relationships (e.g., scatter with regression line; box/violin by category)
- Explain what the relationship suggests

---

### Task 4 — Multivariate Visualizations
- Use color/shape/size encodings or small multiples (facets) to show a third variable
- Add a short interpretation

---

### Task 5 — Temporal or Composition Analysis
- If time exists: line plot(s), rolling averages, or heatmap (e.g., day vs hour)
- If no time: composition (stacked bars or 100% bars) or a treemap/sunburst alternative

---

### Task 6 — Geospatial (Bonus) (Optional)
- If latitude/longitude or regions exist, produce a simple map (choropleth or point map)
- Briefly describe your mapping choices

---

### Task 7 — Aesthetics and Clarity
- Apply a clean theme, readable labels, titles, and legends
- Ensure color choices are colorblind-friendly where possible

---

### Task 8 — Narrative and Reproducibility
- Write a short narrative (5–10 sentences) connecting the plots into a cohesive story
- Ensure the notebook/Rmd runs top-to-bottom with no manual steps

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add brief comments for complex operations
- Ensure both Rmd and Jupyter notebook run top-to-bottom without errors
- Use consistent formatting and follow language-specific style conventions
- Load all required libraries at the beginning of each document

**Visualization Best Practices:**
- Choose appropriate chart types for your data and research questions
- Use clear, descriptive titles and axis labels for all plots
- Apply consistent color schemes and themes throughout your report
- Ensure plots are readable at the size they appear in the final document
- Use colorblind-friendly palettes when possible (avoid red-green combinations)

**Data Storytelling:**
- Create a logical flow from simple to complex visualizations
- Each plot should answer a specific question or reveal an insight
- Provide 2-3 sentence interpretations under each visualization
- Connect your plots into a cohesive narrative that tells a data story
- Highlight the most important findings prominently

**Chart Selection:**
- **Univariate**: Histograms/density plots for numeric, bar charts for categorical
- **Bivariate**: Scatter plots for correlations, box/violin plots for distributions by group
- **Multivariate**: Use color, size, or facets to encode additional variables
- **Temporal**: Line plots for trends, heatmaps for patterns over time
- **Composition**: Stacked/grouped bars, pie charts (sparingly), or treemaps

**Aesthetics and Clarity:**
- Remove unnecessary chart junk (excessive gridlines, borders, backgrounds)
- Use appropriate font sizes and ensure text is readable
- Position legends and annotations to not obscure data
- Maintain consistent spacing and alignment across all plots
- Test how plots look in both screen and print formats

**Documentation:**
- Write clear markdown sections explaining your visualization choices
- Include brief dataset description and any data preprocessing steps
- Document any data quality issues that affect your visualizations
- Provide actionable insights and suggest follow-up analyses

**R Markdown Best Practices (for R submission):**
- Use meaningful chunk names (e.g., `{r univariate-numeric}`)
- Set `echo = TRUE` for code you want to show, `echo = FALSE` for setup
- Use `include = FALSE` for chunks that prepare data but don't need to appear
- Ensure all plots render correctly in PDF format

**Jupyter Notebook Best Practices (for Python submission):**
- Use markdown cells to explain your visualization approach
- Keep code cells focused and well-commented
- Use `%matplotlib inline` for proper plot display
- Ensure plots are saved with appropriate DPI for PDF export

### Deliverables

Submit:

- R: An R Markdown file `Week5_Tasks.Rmd` and `Week5_Tasks.pdf` (knitted to PDF) (10 point)
- Python: A Jupyter Notebook `Week5_Tasks.ipynb` (Optional)(Bonus Point)
(5 point)

Use the provided templates in `Week_05/submission_template/`.

Your submission should include all tasks, plots with captions/annotations, and brief interpretations.

---


