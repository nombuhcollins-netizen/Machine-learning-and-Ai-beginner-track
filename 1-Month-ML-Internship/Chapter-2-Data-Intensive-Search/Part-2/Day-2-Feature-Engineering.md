# Day 2: Feature Engineering & Data Transformation

**Date:** Week 2, Day 2 | **Duration:** 7+ Hours | **Difficulty:** Foundational → Intermediate

---

## 🎯 Learning Objectives

By the end of Day 2, you will:

✅ Convert categorical features to numerical (Label Encoding, One-Hot Encoding)
✅ Scale and normalize numerical features (StandardScaler, MinMaxScaler)
✅ Create feature pipelines for automated transformation
✅ Handle ordinal vs. nominal categories appropriately
✅ Prepare data specifically for scikit-learn models
✅ Understand the difference between fit and transform

---

## 📖 Core Topics

### 1. Label Encoding vs. One-Hot Encoding

#### Label Encoding (Ordinal Categories)
```python
import numpy as np

def label_encode_simple(values):
    """Simple label encoding: convert categories to integers"""
    unique_values = list(set(values))
    mapping = {val: idx for idx, val in enumerate(unique_values)}
    encoded = [mapping[val] for val in values]
    return encoded, mapping

# Usage
colors = ['red', 'blue', 'green', 'red', 'blue']
encoded, mapping = label_encode_simple(colors)
print(encoded)      # [0, 1, 2, 0, 1]
print(mapping)      # {'red': 0, 'blue': 1, 'green': 2}
```

**When to use Label Encoding:**
- Tree-based models (Decision Trees, Random Forest)
- Ordinal categories with natural ordering (small, medium, large)
- Reduce dimensionality (1 column instead of n)

---

#### One-Hot Encoding (Nominal Categories)
```python
def onehot_encode(values):
    """Convert categorical to binary columns"""
    unique_values = list(set(values))
    
    # Create binary matrix
    encoded = []
    for val in values:
        row = [1 if val == uval else 0 for uval in unique_values]
        encoded.append(row)
    
    return np.array(encoded), unique_values

# Usage
colors = ['red', 'blue', 'green', 'red', 'blue']
encoded, categories = onehot_encode(colors)
print(encoded)
# Output:
# [[1 0 0]  <- red
#  [0 1 0]  <- blue
#  [0 0 1]  <- green
#  [1 0 0]  <- red
#  [0 1 0]] <- blue

# With column names
columns = [f'color_{cat}' for cat in categories]
print(columns)  # ['color_red', 'color_blue', 'color_green']
```

**When to use One-Hot Encoding:**
- Linear models (Linear Regression, Logistic Regression)
- No natural ordering between categories
- Neural networks
- Prevents ordinal assumption

**Example: Building a Full Encoder**
```python
class SimpleOneHotEncoder:
    """Class-based one-hot encoder"""
    
    def __init__(self):
        self.categories = {}
    
    def fit(self, column):
        """Learn categories from data"""
        self.categories = list(set(column))
        return self
    
    def transform(self, column):
        """Apply encoding"""
        encoded = []
        for val in column:
            row = [1 if val == cat else 0 for cat in self.categories]
            encoded.append(row)
        return np.array(encoded)
    
    def fit_transform(self, column):
        """Fit and transform in one step"""
        return self.fit(column).transform(column)
    
    def get_feature_names(self):
        """Get names for encoded columns"""
        return self.categories

# Usage
encoder = SimpleOneHotEncoder()
colors = ['red', 'blue', 'green', 'red', 'blue']
encoded = encoder.fit_transform(colors)
print(encoded)
print(encoder.get_feature_names())
```

---

### 2. Feature Scaling & Normalization

#### StandardScaler (Z-score normalization)
```python
import numpy as np

def standardscale(column):
    """Standardize to mean=0, std=1"""
    mean = np.mean(column)
    std = np.std(column)
    return (column - mean) / std

# Usage
ages = np.array([20, 25, 30, 35, 40, 100])  # 100 is outlier
scaled = standardscale(ages)
print(scaled)
# Output: [-1.46 -1.04 -0.63 -0.21  0.21  2.13]

# Verify
print(f"Mean: {np.mean(scaled):.6f}, Std: {np.std(scaled):.6f}")
```

**Advantages:**
- Works well with outliers
- Preserves information about outliers
- Good for distance-based algorithms (KNN, K-means)

---

#### MinMaxScaler (Range normalization)
```python
def minmaxscale(column):
    """Scale to [0, 1] range"""
    min_val = np.min(column)
    max_val = np.max(column)
    return (column - min_val) / (max_val - min_val)

# Usage
salaries = np.array([30000, 50000, 75000, 100000, 150000])
scaled = minmaxscale(salaries)
print(scaled)
# Output: [0.0, 0.267, 0.6, 0.933, 1.0]
```

**Advantages:**
- Bounded output (0 to 1)
- Easy to interpret
- Good for neural networks

---

#### Class-Based Scalers
```python
class StandardScaler:
    """Implements fit/transform pattern"""
    
    def __init__(self):
        self.mean = None
        self.std = None
    
    def fit(self, data):
        """Learn statistics from training data"""
        self.mean = np.mean(data)
        self.std = np.std(data)
        return self
    
    def transform(self, data):
        """Apply scaling"""
        if self.mean is None or self.std is None:
            raise ValueError("Must call fit() first")
        return (data - self.mean) / self.std
    
    def fit_transform(self, data):
        """Fit and transform"""
        return self.fit(data).transform(data)
    
    def inverse_transform(self, scaled_data):
        """Convert back to original scale"""
        return scaled_data * self.std + self.mean

# Usage
scaler = StandardScaler()
train_data = np.array([20, 25, 30, 35, 40])
scaler.fit(train_data)

# Scale training data
train_scaled = scaler.transform(train_data)

# Scale new data with same statistics
new_data = np.array([22, 50])
new_scaled = scaler.transform(new_data)

# Inverse: convert predictions back
predictions_original = scaler.inverse_transform(new_scaled)
```

---

### 3. Feature Engineering Pipeline

#### Building a Complete Pipeline
```python
import pandas as pd
import numpy as np

class FeatureEngineeringPipeline:
    """Complete pipeline for data transformation"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoders = {}
        self.fitted = False
    
    def fit(self, df):
        """Learn transformations from training data"""
        # Fit scalers on numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            self.scaler.fit(df[col].values)
        
        # Fit encoders on categorical columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            encoder = SimpleOneHotEncoder()
            encoder.fit(df[col].values)
            self.encoders[col] = encoder
        
        self.fitted = True
        return self
    
    def transform(self, df):
        """Apply learned transformations"""
        if not self.fitted:
            raise ValueError("Must call fit() first")
        
        result = []
        
        # Transform numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            scaled = self.scaler.transform(df[col].values)
            result.append(scaled)
        
        # Transform categorical columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            encoded = self.encoders[col].transform(df[col].values)
            result.append(encoded)
        
        # Concatenate all
        return np.hstack(result)
    
    def fit_transform(self, df):
        """Fit and transform"""
        return self.fit(df).transform(df)

# Usage Example
df_train = pd.DataFrame({
    'age': [20, 25, 30, 35, 40],
    'salary': [30000, 40000, 50000, 60000, 70000],
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR']
})

pipeline = FeatureEngineeringPipeline()
transformed_train = pipeline.fit_transform(df_train)
print(transformed_train)

# Transform new data
df_new = pd.DataFrame({
    'age': [27],
    'salary': [45000],
    'department': ['IT']
})
transformed_new = pipeline.transform(df_new)
```

---

### 4. ML-Ready Data Preparation

#### Complete Transformation Workflow
```python

class MLDataPreparator:
    """Prepare raw data for ML models"""
    
    def __init__(self, target_column=None):
        self.target_column = target_column
        self.pipeline = FeatureEngineeringPipeline()
        self.feature_names = []
    
    def prepare(self, df, fit=True):
        """Complete preparation workflow"""
        
        # Separate features and target
        if self.target_column:
            X = df.drop(self.target_column, axis=1)
            y = df[self.target_column]
        else:
            X = df
            y = None
        
        # Store feature names
        self.feature_names = list(X.columns)
        
        # Apply transformations
        if fit:
            X_transformed = self.pipeline.fit_transform(X)
        else:
            X_transformed = self.pipeline.transform(X)
        
        return X_transformed, y
    
    def get_feature_info(self):
        """Report on transformed features"""
        return {
            'original_features': self.feature_names,
            'transformed_shape': None,  # Set after transform
            'feature_types': {}
        }

# Usage
df = pd.DataFrame({
    'age': [20, 25, 30, 35, 40],
    'salary': [30000, 40000, 50000, 60000, 70000],
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'hired': [1, 0, 1, 1, 0]
})

prep = MLDataPreparator(target_column='hired')
X, y = prep.prepare(df, fit=True)
print(f"X shape: {X.shape}")  # (5, transformed_features)
print(f"y shape: {y.shape}")  # (5,)
```

---

### 5. Handling Different Feature Types

#### Numerical Features
```python
def process_numerical(df, columns):
    """Process numerical columns"""
    for col in columns:
        # Check for outliers
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        # Cap outliers
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df[col] = df[col].clip(lower, upper)
    
    return df
```

#### Categorical Features
```python
def process_categorical(df, columns, top_n=10):
    """Process categorical columns"""
    for col in columns:
        # Group rare categories
        value_counts = df[col].value_counts()
        top_categories = value_counts.head(top_n).index
        
        df[col] = df[col].apply(
            lambda x: x if x in top_categories else 'OTHER'
        )
    
    return df
```

#### Date/Time Features
```python
def process_datetime(df, columns):
    """Extract features from datetime"""
    for col in columns:
        df[col] = pd.to_datetime(df[col])
        
        # Extract components
        df[f'{col}_year'] = df[col].dt.year
        df[f'{col}_month'] = df[col].dt.month
        df[f'{col}_day'] = df[col].dt.day
        df[f'{col}_dayofweek'] = df[col].dt.dayofweek
        
        # Drop original
        df = df.drop(col, axis=1)
    
    return df
```

---

## 💡 Complete Example: Transform Raw Dataset to ML-Ready

```python
class RawToMLTransformer:
    """Convert raw data to ML-ready format"""
    
    def __init__(self):
        self.pipeline = FeatureEngineeringPipeline()
    
    def clean_and_transform(self, df):
        """Complete transformation"""
        
        # Step 1: Handle missing values
        df = df.dropna()
        
        # Step 2: Remove duplicates
        df = df.drop_duplicates()
        
        # Step 3: Process numerical columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            df[col] = df[col].clip(Q1 - 1.5*IQR, Q3 + 1.5*IQR)
        
        # Step 4: Transform features
        X = self.pipeline.fit_transform(df)
        
        return X
    
    def get_report(self, df):
        """Report on transformation"""
        return {
            'rows_original': len(df),
            'rows_after_cleaning': len(df.dropna()),
            'numeric_cols': len(df.select_dtypes(include=['number']).columns),
            'categorical_cols': len(df.select_dtypes(include=['object']).columns),
            'output_shape': None  # Set after transform
        }

# Usage
df = pd.read_csv('raw_data.csv')
transformer = RawToMLTransformer()
X = transformer.clean_and_transform(df)
print(f"ML-Ready X shape: {X.shape}")
```

---

## � Additional Resources & Learning Links

### **Feature Scaling & Normalization**
- [Scikit-learn Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html) - Official feature scaling documentation
- [StandardScaler vs MinMaxScaler](https://www.kaggle.com/code/rtatman/standardscaler-vs-minmaxscaler) - Kaggle comparison tutorial
- [Feature Scaling Tutorial](https://realpython.com/instance-normalization-cnn/) - Real Python normalization guide

### **Categorical Encoding**
- [One-Hot Encoding Explained](https://en.wikipedia.org/wiki/One-hot) - Wikipedia overview with visuals
- [Label vs One-Hot Encoding](https://www.kdnuggets.com/2021/05/categorical-encoding.html) - KDnuggets comparison
- [Pandas get_dummies()](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html) - Official Pandas encoding function
- [Category Encoders Library](https://contrib.scikit-learn.org/category_encoders/) - Advanced categorical encoding techniques

### **Scikit-learn Pipelines**
- [Creating ML Pipelines](https://scikit-learn.org/stable/modules/pipeline.html) - Official pipeline documentation
- [Pipeline Examples](https://github.com/scikit-learn/scikit-learn/tree/main/examples) - GitHub code examples
- [Why Use Pipelines](https://machinelearningmastery.com/pipelines-in-scikit-learn/) - Machine Learning Mastery guide

### **Feature Engineering Best Practices**
- [Feature Engineering for ML](https://developers.google.com/machine-learning/crash-course/feature-engineering/video-lecture) - Google's ML Crash Course
- ["Tidy Data" Philosophy](https://vita.had.co.nz/papers/tidy-data.pdf) - Essential data organization paper
- [Feature Engineering Course](https://www.kaggle.com/learn/feature-engineering) - Kaggle Learn interactive course

### **Handling Missing Data**
- [pandas.isna() Documentation](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) - Detecting missing values
- [Missing Data Strategies](https://scikit-learn.org/stable/modules/impute.html) - Scikit-learn imputation methods
- [Handling Missing Data](https://www.analyticsvidhya.com/blog/2016/07/missing-value-imputation-one-of-the-most-important-steps-in-data-preprocessing/) - Analytics Vidhya guide

---

## �🔗 Navigation

**[← Back to Chapter 2](../README.md)** | **[Day 2 Exercises →](./Day-2-Exercises.md)**
