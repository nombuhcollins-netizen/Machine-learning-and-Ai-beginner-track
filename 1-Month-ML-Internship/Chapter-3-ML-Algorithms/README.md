# Chapter 3: Machine Learning Algorithms

**Week:** Week 3 | **Duration:** 5 Parts (35+ hours) | **Level:** Intermediate

---

## 🎯 Chapter Objective

Master fundamental ML algorithms by implementing them **from scratch** before using libraries.

By the end of this chapter, you will:
- ✅ Implement linear regression with gradient descent
- ✅ Build classification models (Logistic Regression)
- ✅ Construct decision trees and random forests
- ✅ Reduce dimensionality with PCA
- ✅ Train reinforcement learning agents with Q-Learning
- ✅ Understand when to use each algorithm

---

## 📋 Weekly Structure

| Part | Topic | Core Concepts | Capstone |
|------|-------|---------------|----------|
| **1** | Linear Regression | Gradient descent, MSE, Sigmoid function | GPA Predictor |
| **2** | Classification | Entropy, Gini Impurity, Decision Boundaries | Loan Approval System |
| **3** | Decision Trees & Random Forests | Information Gain, Tree Pruning, Ensemble Methods | Market Basket Analysis |
| **4** | Dimensionality Reduction (PCA) | Eigenvalues, Variance explained, Visualization | Data Compressor |
| **5** | Reinforcement Learning (Q-Learning) | Agents, Environments, Rewards, Q-Learning | Campus Navigation Simulation |

---

## 🏗️ Architecture Philosophy

**Progressive Complexity:** Build algorithms from first principles

- **Part 1:** Understand optimization (gradient descent) & linear prediction
- **Part 2:** Extend to classification (binary prediction with probabilities)
- **Part 3:** Tree-based learning (decision trees & ensembles)
- **Part 4:** Unsupervised learning (dimensionality reduction)
- **Part 5:** Decision-making under uncertainty (reinforcement learning)

**Key Principle:** Math → Code → Scikit-learn comparison

---

## 📂 Directory Structure

```
Chapter-3-ML-Algorithms/
├── README.md (this file)
├── Part-1/
│   ├── Part-1-Linear-Regression.md
│   └── Part-1-Exercises.md
├── Part-2/
│   ├── Part-2-Classification.md
│   └── Part-2-Exercises.md
├── Part-3/
│   ├── Part-3-Decision-Trees.md
│   └── Part-3-Exercises.md
├── Part-4/
│   ├── Part-4-Dimensionality-Reduction.md
│   └── Part-4-Exercises.md
└── Part-5/
    ├── Part-5-Reinforcement-Learning.md
    └── Part-5-Exercises.md
```

---

## 🎓 Learning Outcomes

### By Part 1 (Linear Regression)
- Understand cost functions (MSE)
- Implement gradient descent from scratch
- Build simple linear models
- Tune learning rate and iterations
- Create GPA predictor model

### By Part 2 (Classification)
- Implement logistic regression
- Calculate decision boundaries
- Understand entropy and Gini impurity
- Evaluate with precision/recall/F1
- Build loan approval classifier

### By Part 3 (Decision Trees & Random Forests)
- Build decision trees from scratch
- Understand information gain
- Implement tree pruning
- Build random forests (bagging)
- Analyze feature importance

### By Part 4 (Dimensionality Reduction - PCA)
- Implement PCA from scratch
- Calculate eigenvalues and eigenvectors
- Reduce high-dimensional data
- Visualize with scree plots
- Build data compressor

### By Part 5 (Reinforcement Learning - Q-Learning)
- Understand Markov Decision Processes (MDPs)
- Implement Q-Learning algorithm
- Build agents and environments
- Master exploration vs. exploitation
- Train navigation agent with rewards

---

## 🔧 Technologies and Libraries

### Core Math
```python
NumPy          # Matrix operations
Math           # Basic mathematics
```

### ML Libraries (for comparison)
```python
Scikit-learn   # Production models
```

### Visualization
```python
Matplotlib     # Plotting results
```

---

## 💡 Real-World Applications

1. **Housing Price Prediction** (Part 1)
   - Linear regression on house features
   - Predicting continuous values

2. **Customer Classification** (Part 2)
   - Binary/multiclass classification
   - Predicting customer categories

3. **Decision Trees for Classification** (Part 3)
   - Interpretable models
   - Feature importance analysis from tree splits

4. **High-Dimensional Data Compression** (Part 4)
   - Reducing dimensionality for visualization
   - Feature extraction from image/text data

5. **Autonomous Decision-Making** (Part 5)
   - Agent navigation and pathfinding
   - Robotics and game AI

---

## 📊 Assessment Criteria

### Part Exercises (40%)
- Correct algorithm implementation
- Code efficiency and clarity
- Proper error handling

### Part Capstones (60%)
- Working model on real data
- Proper evaluation metrics
- Comparison with scikit-learn

### Bonus (Extra Credit)
- Advanced optimization techniques
- Hyperparameter tuning
- Cross-validation implementation

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy scikit-learn matplotlib pandas
```

### Workflow
1. Study the Part module content
2. Implement algorithm from scratch
3. Complete exercises
4. Build capstone project
5. Compare with scikit-learn implementation

---

## 📚 Core Concepts Map

```
PART 1: LINEAR REGRESSION
  Cost Function → Gradient Descent → Parameter Update
  
PART 2: CLASSIFICATION (Extends Part 1)
  Logistic Function → Cross-Entropy Loss → Decision Boundary
  
PART 3: DECISION TREES & RANDOM FORESTS
  Information Gain → Tree Construction → Ensemble Methods
  
PART 4: DIMENSIONALITY REDUCTION (PCA)
  Covariance Matrix → Eigendecomposition → PCA Projection
  
PART 5: REINFORCEMENT LEARNING (Q-Learning)
  Agents → Environments → Rewards → Bellman Equation → Q-Updates
```

---

## 🔗 Navigation

- **[← Back to Main](../README.md)**
- **[Part 1: Linear Regression →](./Part-1/)**

---

## 💬 Key ML Principles

1. **Learning Paradigms**
   - Parts 1-3: Supervised Learning (with labeled data)
   - Part 4: Unsupervised Learning (PCA for feature extraction)
   - Part 5: Reinforcement Learning (learn from interaction)

2. **Bias-Variance Tradeoff**
   - Complex models overfit
   - Simple models underfit
   - Find balance through validation

3. **Model Evaluation**
   - Train/test split essential
   - Use appropriate metrics per task
   - Cross-validation for robustness

4. **Feature Engineering**
   - Not all features equally important
   - Proper scaling and normalization needed
   - Feature selection and reduction crucial

5. **Algorithm Selection**
   - Linear data → linear models (Part 1)
   - Complex patterns → trees/forests (Part 3)
   - High dimensions → PCA (Part 4)
   - Decision-making → RL agents (Part 5)

---

**Last Updated:** February 19, 2026 | **Status:** Ready for implementation
