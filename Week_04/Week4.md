## Week 4 Tasks — Advanced Data Analysis and Modeling (R)

Week 4 continues the data analysis workflow from Week 3, focusing on advanced modeling techniques and evaluation. Your submission must be in R Markdown. Use the same dataset from Week 3 or choose a new one if preferred.

Reference dataset (optional): [Uber Data Analytics Dashboard](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)

Guidance:
- Build upon the foundation from Week 3 tasks 1-5
- Focus on model improvement and thorough evaluation
- Keep code reproducible; avoid manual steps

---

### Task 1 — Class Imbalance (if applicable)
- If classification target exists, assess class proportions and apply one strategy if imbalance exists.

---

### Task 2 — Feature Engineering
- Create/transform at least 2 features useful for modeling; drop irrelevant columns if needed.

---

### Task 3 — Baseline Modeling
- Train a simple baseline model suitable for your problem (classification or regression). Show training code and predictions.

---

### Task 4 — Evaluation
- Use appropriate metrics and provide a short interpretation (2–4 sentences).

---

### Task 5 — Findings and Next Steps
- Summarize 3–5 insights and propose 2 next steps to improve the analysis/model.

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

Submit an R Markdown document only (template provided in `Week_04/submission_template/`):

- `Week4_Tasks.Rmd` (knit to PDF)

Your submission must include solutions to all tasks, with runnable code and brief annotations under results.


