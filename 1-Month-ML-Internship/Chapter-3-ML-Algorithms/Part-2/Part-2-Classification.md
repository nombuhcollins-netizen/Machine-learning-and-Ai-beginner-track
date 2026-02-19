# Part 2: Classification & Logistic Regression

**Week:** Week 3, Part 2 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

By the end of Part 2, you will:

✅ Understand classification vs regression
✅ Implement logistic sigmoid function
✅ Build logistic regression from scratch
✅ Calculate cross-entropy loss
✅ Evaluate with classification metrics (precision, recall, F1)
✅ Handle binary and multiclass classification

---

## 📖 Core Topics

### 1. Classification Fundamentals

#### Binary Classification
```python
# Problem: Predict if something belongs to class 0 or 1
# Example: Is email spam or not spam?

import numpy as np

# Sample binary data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # Features
y = np.array([0, 0, 1, 1])  # Binary classes
```

#### Sigmoid Function
```python
def sigmoid(z):
    """
    Sigmoid function: converts z to probability [0, 1]
    σ(z) = 1 / (1 + e^-z)
    """
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))  # clip to prevent overflow

# Properties:
# - sigmoid(-inf) = 0
# - sigmoid(0) = 0.5
# - sigmoid(+inf) = 1
# - Always output between 0 and 1

# Visualization
z = np.linspace(-10, 10, 100)
probabilities = sigmoid(z)
```

---

### 2. Logistic Regression

#### Implementation from Scratch
```python
class LogisticRegression:
    """Binary logistic regression classifier"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.w = None
        self.b = None
        self.losses = []
    
    def fit(self, X, y):
        """Fit model using gradient descent"""
        n, m = X.shape  # n samples, m features
        
        # Initialize weights and bias
        self.w = np.zeros(m)
        self.b = 0
        
        for i in range(self.iterations):
            # Linear combination
            z = X @ self.w + self.b
            
            # Sigmoid activation
            y_pred = sigmoid(z)
            
            # Calculate gradients (cross-entropy loss)
            # dL/dw = (1/n) * X^T @ (y_pred - y)
            # dL/db = (1/n) * sum(y_pred - y)
            
            dw = (1/n) * X.T @ (y_pred - y)
            db = (1/n) * np.sum(y_pred - y)
            
            # Update parameters
            self.w -= self.lr * dw
            self.b -= self.lr * db
            
            # Calculate loss (cross-entropy)
            # For numerical stability:
            loss = -np.mean(y * np.log(y_pred + 1e-15) + 
                           (1 - y) * np.log(1 - y_pred + 1e-15))
            self.losses.append(loss)
            
            if (i + 1) % 100 == 0:
                print(f"Iteration {i+1}: Loss = {loss:.4f}")
        
        return self
    
    def predict_proba(self, X):
        """Predict class probabilities"""
        z = X @ self.w + self.b
        return sigmoid(z)
    
    def predict(self, X, threshold=0.5):
        """Make binary predictions"""
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

# Usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)
predictions = model.predict(X)
probabilities = model.predict_proba(X)
```

---

### 3. Loss Functions

#### Cross-Entropy Loss
```python
def cross_entropy_loss(y_true, y_pred):
    """Calculate cross-entropy loss"""
    n = len(y_true)
    # Add small epsilon for numerical stability
    eps = 1e-15
    loss = -np.mean(
        y_true * np.log(y_pred + eps) + 
        (1 - y_true) * np.log(1 - y_pred + eps)
    )
    return loss

# Properties:
# - Equals 0 when predictions are perfect
# - Approaches infinity for wrong predictions
# - Penalizes confident wrong predictions heavily
```

---

### 4. Classification Metrics

#### Confusion Matrix and Metrics
```python
def confusion_matrix(y_true, y_pred):
    """Calculate confusion matrix"""
    tp = np.sum((y_pred == 1) & (y_true == 1))  # True Positive
    tn = np.sum((y_pred == 0) & (y_true == 0))  # True Negative
    fp = np.sum((y_pred == 1) & (y_true == 0))  # False Positive
    fn = np.sum((y_pred == 0) & (y_true == 1))  # False Negative
    
    return np.array([[tn, fp], [fn, tp]])

def precision(y_true, y_pred):
    """Precision: TP / (TP + FP)"""
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    return tp / (tp + fp) if (tp + fp) > 0 else 0

def recall(y_true, y_pred):
    """Recall: TP / (TP + FN)"""
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fn = np.sum((y_pred == 0) & (y_true == 1))
    return tp / (tp + fn) if (tp + fn) > 0 else 0

def f1_score(y_true, y_pred):
    """F1 Score: 2 * (precision * recall) / (precision + recall)"""
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * (p * r) / (p + r) if (p + r) > 0 else 0

def accuracy(y_true, y_pred):
    """Accuracy: (TP + TN) / Total"""
    return np.mean(y_true == y_pred)

# Usage
y_true = np.array([0, 0, 1, 1, 1])
y_pred = np.array([0, 1, 1, 1, 0])

print(f"Accuracy: {accuracy(y_true, y_pred):.3f}")
print(f"Precision: {precision(y_true, y_pred):.3f}")
print(f"Recall: {recall(y_true, y_pred):.3f}")
print(f"F1 Score: {f1_score(y_true, y_pred):.3f}")
```

---

### 5. Multiclass Classification

#### One-vs-Rest (OvR)
```python
class MulticlassLogisticRegression:
    """Multiclass using one-vs-rest strategy"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.models = {}
        self.classes = None
    
    def fit(self, X, y):
        """Fit binary classifier for each class"""
        self.classes = np.unique(y)
        
        for cls in self.classes:
            # Binary problem: class vs rest
            y_binary = (y == cls).astype(int)
            
            # Train binary classifier
            model = LogisticRegression(self.lr, self.iterations)
            model.fit(X, y_binary)
            self.models[cls] = model
        
        return self
    
    def predict_proba(self, X):
        """Get probability for each class"""
        probas = []
        
        for cls in self.classes:
            proba = self.models[cls].predict_proba(X)
            probas.append(proba)
        
        # Normalize (softmax-like)
        probas = np.column_stack(probas)
        return probas / probas.sum(axis=1, keepdims=True)
    
    def predict(self, X):
        """Predict class with highest probability"""
        probas = self.predict_proba(X)
        return self.classes[np.argmax(probas, axis=1)]

# Usage
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 2, 2])

model = MulticlassLogisticRegression()
model.fit(X, y)
predictions = model.predict(X)
probabilities = model.predict_proba(X)
```

---

## 💡 Complete Example: Email Spam Classifier

```python
class SpamClassifier:
    """Email spam/ham classifier"""
    
    def __init__(self):
        self.model = LogisticRegression(lr=0.01, iterations=1000)
        self.scaler = StandardScaler()
    
    def preprocess(self, X, fit=False):
        """Scale features"""
        if fit:
            return self.scaler.fit_transform(X)
        return self.scaler.transform(X)
    
    def fit(self, X, y):
        """Fit model"""
        X_scaled = self.preprocess(X, fit=True)
        self.model.fit(X_scaled, y)
        return self
    
    def predict(self, X):
        """Predict spam (1) or ham (0)"""
        X_scaled = self.preprocess(X)
        return self.model.predict(X_scaled)
    
    def predict_proba(self, X):
        """Get spam probability"""
        X_scaled = self.preprocess(X)
        return self.model.predict_proba(X_scaled)
    
    def evaluate(self, y_true, y_pred):
        """Calculate metrics"""
        return {
            'accuracy': accuracy(y_true, y_pred),
            'precision': precision(y_true, y_pred),
            'recall': recall(y_true, y_pred),
            'f1': f1_score(y_true, y_pred)
        }
```

---

## � Additional Resources & Learning Links

### **Classification Algorithms**
- [Classification (Wikipedia)](https://en.wikipedia.org/wiki/Statistical_classification) - Overview of classification in machine learning
- [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression) - Mathematical foundations
- [Support Vector Machines](https://en.wikipedia.org/wiki/Support_vector_machine) - SVM theory and applications

### **Scikit-learn Classification**
- [Scikit-learn Classifiers](https://scikit-learn.org/stable/modules/classification.html) - Complete classification module docs
- [Logistic Regression API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) - Implementation and parameters
- [SVM API](https://scikit-learn.org/stable/modules/svm.html) - Support vector machines

### **Classification Metrics**
- [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix) - Wikipedia reference with formulas
- [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall) - Evaluation metrics explained
- [ROC and AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) - ROC curves for classification

### **Decision Boundaries**
- [Decision Boundaries in ML](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html) - Visualizing decision regions
- [Linear vs Non-linear](https://en.wikipedia.org/wiki/Linear_separability) - Linear separability concepts
- [Kernel Methods](https://en.wikipedia.org/wiki/Kernel_method) - Non-linear decision boundaries

### **StatQuest Videos**
- [Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgC22) - Josh Starmer visual explanation
- [SVM Clearly Explained](https://www.youtube.com/watch?v=efR1C6CvhmE) - StatQuest SVM tutorial
- [ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM) - Classification evaluation

---

## �🔗 Navigation

**[← Back to Chapter 3](../README.md)** | **[Part 2 Exercises →](./Part-2-Exercises.md)**
