## Week 7 Tasks — Introduction to TensorBoard

TensorBoard is a powerful visualization toolkit for machine learning workflows. This week focuses on understanding TensorBoard's core features through simple examples. You'll learn to track training metrics, visualize model architectures, and monitor training progress.

Reference datasets (choose one or use your own):
- [MNIST Handwritten Digits](https://www.tensorflow.org/datasets/catalog/mnist) - Classic image classification
- [Boston Housing](https://www.tensorflow.org/datasets/catalog/boston_housing) - Regression dataset
- [Iris Flowers](https://www.tensorflow.org/datasets/catalog/iris) - Simple classification dataset

Guidance: Start with simple models to focus on TensorBoard features rather than complex model architectures.

Tutorial page: [TensorBoard](https://www.tensorflow.org/tensorboard/get_started)
Pytorch TensorBoard: [Pytorch TensorBoard](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
---

### Task 1 — Basic TensorBoard Setup and Logging
- Install and import TensorBoard dependencies
- Create a simple neural network model (e.g., for MNIST or Iris classification)
- Set up TensorBoard logging
- Train the model for a few epochs and verify logs are created
- Launch TensorBoard and navigate to the Scalars tab

---

### Task 2 — Training Metrics Visualization
- Train your model with TensorBoard logging enabled
- View loss and accuracy curves in TensorBoard
- Experiment with different learning rates and compare results
- Add custom metrics (e.g., precision, recall) to your model
- Document the training progress and any insights from the metrics

---

### Task 3 — Model Architecture Visualization
- Use TensorBoard's Graphs tab to visualize your model architecture
- Create a more complex model (add more layers, different activation functions)
- Compare different model architectures side by side
- Export and save model graphs
- Explain the model structure and data flow

---

### Task 4 — Hyperparameter Tuning and Comparison
- Train multiple models with different hyperparameters (learning rate, batch size, number of layers)
- Use TensorBoard to compare training curves across different runs
- Create a summary of best performing configurations
- Document insights about how hyperparameters affect model performance
- Save the best model and its TensorBoard logs

---

### Guidelines

**Code Quality:**
- Use clear, readable variable names and add comments for TensorBoard-specific code
- Ensure the Jupyter notebook runs top-to-bottom without errors
- Use consistent formatting and follow Python/TensorFlow conventions
- Load all required libraries at the beginning of the notebook

**TensorBoard Best Practices:**
- Use descriptive run names for different experiments
- Organize logs in separate directories for different runs
- Include meaningful comments in your model architecture
- Save model checkpoints for reproducibility
- Document your hyperparameter choices and reasoning

**Model Development:**
- Start with simple models to focus on TensorBoard features
- Use appropriate data preprocessing for your chosen dataset
- Implement proper train/validation splits
- Use early stopping to prevent overfitting
- Save model weights and architecture

**Visualization and Analysis:**
- Take screenshots of important TensorBoard visualizations
- Explain what each visualization tells you about your model
- Compare different model configurations clearly
- Document insights about training dynamics
- Provide actionable recommendations based on results

**Documentation Requirements:**
- Explain your model architecture choices
- Document hyperparameter tuning process
- Include TensorBoard screenshots with captions
- Provide interpretation of training curves
- Summarize key findings and recommendations

### Deliverables

Submit a Jupyter Notebook `Week7_Tasks.ipynb` (8 points) and screenshots of TensorBoard (2 points)

Your submission should include:
- All 4 tasks completed with working code
- TensorBoard visualizations with screenshots and explanations
- Model training logs and comparisons
- Clear documentation of findings and insights

---

### Evaluation Criteria

**TensorBoard Setup (25%):**
- Proper installation and configuration
- Successful logging setup
- Correct TensorBoard launch and navigation

**Training Metrics (25%):**
- Effective use of scalar logging
- Clear visualization of training progress
- Meaningful metric comparisons

**Model Architecture (25%):**
- Successful model graph visualization
- Clear explanation of model structure
- Comparison of different architectures

**Hyperparameter Tuning (25%):**
- Systematic hyperparameter experimentation
- Effective use of TensorBoard for comparison
- Clear documentation of findings and recommendations

**Code Quality and Documentation:**
- Clean, readable, and well-commented code
- Proper TensorFlow/Keras best practices
- Comprehensive documentation of TensorBoard usage
- Reproducible experiments and clear insights