# Day 3: Data Visualization & Exploratory Data Analysis

**Date:** Week 2, Day 3 | **Duration:** 7+ Hours | **Difficulty:** Foundational → Intermediate

---

## 🎯 Learning Objectives

By the end of Day 3, you will:

✅ Create publication-quality visualizations with Matplotlib and Seaborn
✅ Master univariate, bivariate, and multivariate plotting
✅ Identify correlations and outliers visually
✅ Perform exploratory data analysis (EDA) systematically
✅ Generate insights from visual patterns
✅ Create comprehensive analysis reports

---

## 📖 Core Topics

### 1. Matplotlib Fundamentals

#### Basic Plot Creation
```python
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', linewidth=2, label='Linear')
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.title('Simple Line Plot', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Histogram
```python
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Data')
plt.show()
```

#### Scatter Plot
```python
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=50, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()
```

#### Box Plot
```python
data = [np.random.normal(0, 1, 100), 
        np.random.normal(3, 1, 100),
        np.random.normal(1, 2, 100)]

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=['Group A', 'Group B', 'Group C'])
plt.ylabel('Value')
plt.title('Box Plot Comparison')
plt.show()
```

---

### 2. Seaborn for Statistical Visualization

#### Stylistic Enhancements
```python
import seaborn as sns
import pandas as pd

# Set style
sns.set_style("whitegrid")  # or "darkgrid", "dark", "white", "ticks"
sns.set_palette("husl")  # or "viridis", "rocket", etc.

# Heatmap
df = pd.DataFrame(np.random.randn(10, 10))
plt.figure(figsize=(10, 8))
sns.heatmap(df, cmap='coolwarm', annot=True, fmt='.1f')
plt.title('Correlation Matrix')
plt.show()
```

#### Relational Plots
```python
# Scatter plot with categories
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', hue='category', s=100)
plt.title('Scatter Plot by Category')
plt.show()
```

#### Distribution Plots
```python
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='x', kde=True, bins=30)
plt.title('Distribution')
plt.show()
```

---

### 3. Correlation Analysis

#### Computing Correlations
```python
import pandas as pd

df = pd.DataFrame({
    'age': [20, 25, 30, 35, 40, 45],
    'salary': [30000, 40000, 50000, 60000, 70000, 80000],
    'experience': [1, 2, 5, 8, 12, 15]
})

# Correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# Specific correlation
correlation = df['age'].corr(df['salary'])
print(f"Correlation: {correlation:.3f}")
```

#### Visualizing Correlations
```python
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0, 
            vmin=-1, vmax=1, square=True)
plt.title('Correlation Matrix')
plt.show()
```

#### Identifying Strong Correlations
```python
def get_top_correlations(df, target_col, n=5):
    """Get top correlations with target variable"""
    correlations = df.corr()[target_col].sort_values(ascending=False)
    return correlations[1:n+1]  # Exclude self-correlation

# Usage
top_corr = get_top_correlations(df, 'salary', n=5)
print(top_corr)
```

---

### 4. Outlier Detection

#### Visual Outlier Detection
```python
# Box plot for outlier detection
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='salary')
plt.title('Salary Distribution (Outliers visible)')
plt.show()

# Identify outliers via IQR
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['salary'] < Q1 - 1.5*IQR) | (df['salary'] > Q3 + 1.5*IQR)]
print(f"Found {len(outliers)} outliers")
```

---

### 5. Multi-Panel Visualizations

#### Creating Dashboards
```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Histogram
axes[0, 0].hist(df['age'], bins=20, color='blue', edgecolor='black')
axes[0, 0].set_title('Age Distribution')

# Plot 2: Scatter
axes[0, 1].scatter(df['age'], df['salary'], alpha=0.6)
axes[0, 1].set_title('Age vs Salary')

# Plot 3: Box plot
axes[1, 0].boxplot([df['age'], df['salary']])
axes[1, 0].set_title('Distributions')

# Plot 4: Correlation heatmap
sns.heatmap(df.corr(), ax=axes[1, 1], cmap='coolwarm', annot=True)
axes[1, 1].set_title('Correlations')

plt.tight_layout()
plt.show()
```

---

## 💡 Complete Example: EDA System

```python
class DataVisualizer:
    """Complete EDA and visualization system"""
    
    def __init__(self, df):
        self.df = df
        sns.set_style("whitegrid")
    
    def plot_distributions(self):
        """Plot all numerical distributions"""
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        n_cols = len(numeric_cols)
        
        fig, axes = plt.subplots((n_cols + 1) // 2, 2, figsize=(12, n_cols * 3))
        axes = axes.flatten()
        
        for idx, col in enumerate(numeric_cols):
            axes[idx].hist(self.df[col], bins=30, edgecolor='black')
            axes[idx].set_title(f'Distribution of {col}')
        
        plt.tight_layout()
        return fig
    
    def plot_correlations(self):
        """Plot correlation matrix"""
        fig, ax = plt.subplots(figsize=(10, 8))
        numeric_df = self.df.select_dtypes(include=['number'])
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', 
                    center=0, ax=ax, vmin=-1, vmax=1)
        plt.title('Feature Correlations')
        return fig
    
    def plot_outliers(self):
        """Plot box plots for outlier detection"""
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        n_cols = len(numeric_cols)
        
        fig, axes = plt.subplots(1, n_cols, figsize=(n_cols * 4, 5))
        if n_cols == 1:
            axes = [axes]
        
        for idx, col in enumerate(numeric_cols):
            axes[idx].boxplot([self.df[col]])
            axes[idx].set_title(f'{col}')
        
        plt.tight_layout()
        return fig
    
    def plot_relationships(self, x_col, y_col):
        """Plot relationship between two variables"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.scatter(self.df[x_col], self.df[y_col], alpha=0.6, s=50)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f'{x_col} vs {y_col}')
        
        # Add correlation
        corr = self.df[x_col].corr(self.df[y_col])
        ax.text(0.05, 0.95, f'Correlation: {corr:.3f}', 
                transform=ax.transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        return fig
    
    def generate_report(self, output_file='eda_report.png'):
        """Generate multi-figure report"""
        print("Generating EDA report...")
        
        self.plot_distributions()
        plt.savefig('distributions.png', dpi=300, bbox_inches='tight')
        
        self.plot_correlations()
        plt.savefig('correlations.png', dpi=300, bbox_inches='tight')
        
        self.plot_outliers()
        plt.savefig('outliers.png', dpi=300, bbox_inches='tight')
        
        print(f"Report saved!")

# Usage
viz = DataVisualizer(df)
viz.generate_report()
```

---

## 🔗 Navigation

**[← Back to Chapter 2](../README.md)** | **[Day 3 Exercises →](./Day-3-Exercises.md)**
