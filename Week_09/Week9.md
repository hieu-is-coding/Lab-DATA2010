## Week 9 Tasks — Data Mining with Python

This week focuses on fundamental data mining techniques using Python. You'll explore association rule mining, clustering algorithms, classification, and anomaly detection. These techniques are essential for discovering patterns, grouping similar data points, and identifying outliers in datasets.

Reference datasets (choose one or use your own):
- [Market Basket Analysis Dataset](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis) - For association rule mining
- [Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) - For clustering
- [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) - For anomaly detection
- [Iris Dataset](https://www.kaggle.com/datasets/uciml/iris) - Classic dataset for classification
- [Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset) - Multi-class classification

Guidance: Start with smaller datasets to understand the algorithms, then apply them to more complex datasets. Focus on understanding the parameters and interpreting results.

Some tutorials:
- Scikit-learn Documentation: [Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- MLxtend Library: [Association Rules](https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/)
- Scikit-learn: [Anomaly Detection](https://scikit-learn.org/stable/modules/outlier_detection.html)

---

### Task 1 — Association Rule Mining

- Load a transactional dataset suitable for market basket analysis
- Use the Apriori algorithm to find frequent itemsets
- Generate association rules with support, confidence, and lift metrics
- Filter rules based on minimum support and confidence thresholds
- Visualize the top association rules (e.g., using network graphs or bar charts)
- Interpret the most interesting rules and explain their business implications

---

### Task 2 — Clustering Analysis

- Load a dataset with multiple numeric features suitable for clustering
- Apply K-means clustering with different numbers of clusters (k=2, 3, 4, 5)
- Use the elbow method to determine the optimal number of clusters
- Visualize clusters using 2D scatter plots (use PCA if needed for dimensionality reduction)
- Calculate and interpret cluster characteristics (centroids, within-cluster sum of squares)
- Apply DBSCAN clustering and compare results with K-means
- Document the differences between the two clustering approaches

---

### Task 3 — Classification with Decision Trees

- Load a classification dataset with both features and target labels
- Split the data into training and testing sets
- Train a Decision Tree classifier
- Visualize the decision tree structure
- Evaluate the model using accuracy, precision, recall, and F1-score
- Create a confusion matrix and interpret the results
- Experiment with different tree parameters (max_depth, min_samples_split) and compare results
- Identify the most important features for classification

---

### Task 4 — Anomaly Detection

- Load a dataset suitable for anomaly detection (or use a normal dataset and introduce anomalies)
- Apply Isolation Forest for anomaly detection
- Use Local Outlier Factor (LOF) as an alternative method
- Visualize normal vs. anomalous data points
- Compare the results from both methods
- Calculate the percentage of anomalies detected
- Interpret what makes the detected points anomalous

---

### Task 5 — Model Evaluation and Comparison

- Compare the performance of different classification algorithms (Decision Tree, Random Forest, K-Nearest Neighbors)
- Use cross-validation to evaluate model stability
- Create ROC curves and calculate AUC scores (for binary classification)
- Generate classification reports for all models
- Visualize model comparison using bar charts or tables
- Select the best performing model and justify your choice

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add comments for algorithm-specific code
- Ensure the Jupyter notebook runs top-to-bottom without errors
- Use consistent formatting and follow Python conventions
- Load all required libraries at the beginning of the notebook
- Use appropriate data structures (DataFrames, arrays) for different operations

**Data Mining Best Practices:**
- Preprocess data appropriately (normalization, encoding) before applying algorithms
- Use appropriate distance metrics for clustering (Euclidean, Manhattan, etc.)
- Set meaningful thresholds for association rules (support, confidence)
- Handle missing values and outliers appropriately
- Document parameter choices and their impact on results

**Algorithm Understanding:**
- Explain how each algorithm works conceptually
- Discuss the assumptions and limitations of each method
- Interpret results in the context of your dataset
- Compare different algorithms and explain when to use each
- Document hyperparameter tuning process

**Visualization and Analysis:**
- Create clear visualizations for each technique
- Use appropriate plot types (scatter plots for clusters, network graphs for rules, etc.)
- Add meaningful titles, labels, and legends to all plots
- Interpret visualizations and explain insights
- Highlight key findings and patterns discovered

**Documentation Requirements:**
- Explain your dataset choice and preprocessing steps
- Document algorithm parameters and their rationale
- Include interpretations of results for each task
- Compare different methods and explain trade-offs
- Provide actionable insights and recommendations
- Summarize key findings and patterns discovered

**Libraries and Tools:**
- **Pandas & NumPy**: Data manipulation and numerical operations
- **Scikit-learn**: Clustering, classification, and anomaly detection
- **MLxtend**: Association rule mining (Apriori algorithm)
- **Matplotlib & Seaborn**: Visualization
- **Scipy**: Statistical operations and distance metrics

---

### Deliverables

Submit a Jupyter Notebook `Week9_Tasks.ipynb` (10 points)

Your submission should include:
- All 5 tasks completed with working code
- Visualizations for each data mining technique
- Model evaluations and comparisons
- Clear documentation of findings and insights
- Interpretation of results and business implications

---

### Evaluation Criteria

**Association Rule Mining (20%):**
- Proper implementation of Apriori algorithm
- Appropriate threshold selection
- Clear visualization of rules
- Meaningful interpretation of results

**Clustering Analysis (25%):**
- Correct implementation of K-means and DBSCAN
- Appropriate determination of optimal number of clusters
- Clear visualization of clusters
- Comparison and interpretation of clustering methods

**Classification (25%):**
- Proper implementation of Decision Tree classifier
- Appropriate model evaluation metrics
- Clear visualization of decision tree
- Feature importance analysis

**Anomaly Detection (15%):**
- Correct implementation of anomaly detection methods
- Appropriate visualization of anomalies
- Comparison of different methods
- Clear interpretation of detected anomalies

**Model Evaluation and Comparison (15%):**
- Comprehensive model comparison
- Appropriate use of evaluation metrics
- Clear visualization of model performance
- Justified selection of best model

**Code Quality and Documentation:**
- Clean, readable, and well-commented code
- Proper use of Python and data mining libraries
- Comprehensive documentation of methods and results
- Reproducible experiments and clear insights

