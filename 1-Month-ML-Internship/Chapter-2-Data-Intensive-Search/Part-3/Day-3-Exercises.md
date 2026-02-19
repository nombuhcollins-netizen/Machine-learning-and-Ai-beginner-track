# Day 3: Data Visualization & EDA - Exercises

**Difficulty:** Foundational → Intermediate | **Time:** 6-7 hours | **Capstone:** Insights Report

---

## 📝 Exercise Set 1: Matplotlib Basics

### Exercise 1.1: Plot Types
Create scripts to plot:
- Line plot (time series data)
- Histogram (distribution)
- Scatter plot (relationships)
- Bar plot (categories)

**File:** `matplotlib_basics.py`

**Success Criteria:**
- [ ] All 4 plot types created
- [ ] Labels and titles present
- [ ] Color and markers customized
- [ ] Legends displayed

---

### Exercise 1.2: Multi-Panel Layouts
Create 2×2 subplot layout with:
- Top-left: Histogram
- Top-right: Scatter plot
- Bottom-left: Box plot
- Bottom-right: Bar chart

**File:** `subplot_layouts.py`

---

### Exercise 1.3: Styling and Customization
Customize plots with:
- Different color schemes
- Font sizes and styles
- Grid settings
- Save with high DPI

**File:** `plotting_styles.py`

---

## 📝 Exercise Set 2: Seaborn Advanced

### Exercise 2.1: Statistical Plots
Create:
- Distribution plots with KDE
- Box plots by category
- Violin plots
- Count plots

**File:** `seaborn_statistical.py`

---

### Exercise 2.2: Relationship Plots
Create:
- Scatter plots with hue
- Regression plots with CI
- Pair plots (for small datasets)
- Joint plots

**File:** `seaborn_relationships.py`

---

### Exercise 2.3: Heatmaps and Clustering
Create:
- Correlation heatmap
- Clustered heatmap
- Annotated heatmap
- With custom colormaps

**File:** `seaborn_heatmaps.py`

---

## 📝 Exercise Set 3: Correlation Analysis

### Exercise 3.1: Compute Correlations
Create function that:
- Computes correlation matrix
- Identifies strong correlations (>0.7)
- Reports findings
- Visualizes results

**File:** `correlation_analysis.py`

```python
def analyze_correlations(df, threshold=0.7):
    """Find and report strong correlations"""
    corr_matrix = df.corr()
    strong_corrs = []
    
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                strong_corrs.append({
                    'var1': corr_matrix.columns[i],
                    'var2': corr_matrix.columns[j],
                    'correlation': corr_matrix.iloc[i, j]
                })
    
    return pd.DataFrame(strong_corrs)
```

---

### Exercise 3.2: Feature Importance via Correlation
Identify features most correlated with target:

**File:** `feature_correlation_ranking.py`

```python
def rank_features_by_correlation(df, target_col, n=10):
    """Rank features by correlation with target"""
    correlations = df.corr()[target_col].abs().sort_values(ascending=False)
    return correlations[1:n+1]  # Exclude self
```

---

### Exercise 3.3: Multicollinearity Detection
Create function that:
- Identifies highly correlated features
- Suggests feature removal
- Visualizes correlation networks

**File:** `multicollinearity_detection.py`

---

## 📝 Exercise Set 4: Outlier Detection

### Exercise 4.1: IQR-Based Detection
Identify outliers using IQR method:

**File:** `iqr_outlier_detection.py`

```python
def find_outliers_iqr(data):
    """Find outliers using IQR method"""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers, lower_bound, upper_bound
```

---

### Exercise 4.2: Z-Score Method
Identify outliers using Z-score:

**File:** `zscore_outlier_detection.py`

```python
def find_outliers_zscore(data, threshold=3):
    """Find outliers using Z-score"""
    z_scores = np.abs((data - data.mean()) / data.std())
    return data[z_scores > threshold]
```

---

### Exercise 4.3: Visualize Outliers
Create visualization showing:
- Box plots with outliers highlighted
- Distribution with outlier threshold lines
- Scatter plot with outliers colored differently

**File:** `visualize_outliers.py`

---

## 📝 Exercise Set 5: Comprehensive EDA

### Exercise 5.1: EDA Report Directory
Create function that generates multiple analysis plots:

**File:** `comprehensive_eda.py`

```python
def generate_eda_plots(df, output_dir='eda_plots'):
    os.makedirs(output_dir, exist_ok=True)
    
    # Distribution plots
    # Correlation plots
    # Outlier plots
    # Relationship plots
    
    print(f"Saved {n_plots} plots to {output_dir}")
```

---

### Exercise 5.2: Statistical Summary Report
Create text report with:
- Description of each column
- Missing value percentages
- Unique values for categorical
- Mean/median/std for numerical
- Top values for categorical

**File:** `statistical_summary.py`

---

### Exercise 5.3: Interactive Dashboard (Optional)
Use Streamlit to create interactive dashboard:

**File:** `dashboard_app.py`

---

## 🎯 Capstone: Insights Report

### Project: Generate Analysis Report with 5 Visual Charts

**Scenario:**
You're given a dataset and must:
1. Analyze data thoroughly
2. Create 5 insightful visualizations
3. Write explanations for each
4. Generate HTML report

**Deliverables:**

#### Part 1: Load & Explore (`part1_explore.py`)
- Load dataset
- Initial EDA
- Identify columns and types
- Report basic statistics

#### Part 2: Create 5 Charts (`part2_visualizations.py`)

**Chart 1: Distribution Analysis**
- Histogram of most important numerical feature
- With KDE overlay
- Show mean/median lines
- Title: "Feature Distribution"

**Chart 2: Correlation Heatmap**
- Correlation matrix for numerical features
- With annotations
- Color scale from -1 to 1
- Title: "Feature Correlations"

**Chart 3: Outlier Analysis**
- Box plot showing outliersfor key features
- Identify and count outliers
- Title: "Outlier Detection"

**Chart 4: Categorical Analysis**
- Count plot or pie chart of categorical feature
- Top 5 or 10 categories
- Title: "Category Distribution"

**Chart 5: Key Relationship**
- Scatter plot between two strongly correlated features
- Color by third variable if available
- Include correlation coefficient
- Title: "Feature Relationship"

#### Part 3: Explanations (`part3_explanations.txt`)
For each chart, write:
- What the chart shows
- Key insight
- Why it's important for analysis

#### Part 4: Generate HTML Report (`part4_report_generator.py`)
```python
def generate_html_report(charts_dict, explanations_dict, output_file='report.html'):
    """Create professional HTML report"""
    # Embed charts as images
    # Add explanations
    # Add summary statistics
    # Save as HTML
```

**Report Structure:**
```html
<html>
  <h1>Data Analysis Report</h1>
  
  <h2>Executive Summary</h2>
  - Dataset overview
  - Key findings
  
  <h2>Chart 1: ...</h2>
  - Image
  - Explanation
  
  ... (repeat for 5 charts)
  
  <h2>Conclusions</h2>
  - Main insights
  - Recommendations
</html>
```

#### Part 5: Testing (`part5_test.py`)
```python
if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    
    # Generate all visualizations
    charts = create_visualizations(df)
    
    # Save as images
    for name, fig in charts.items():
        fig.savefig(f'{name}.png', dpi=300, bbox_inches='tight')
    
    # Generate report
    generate_html_report(charts, explanations, 'report.html')
```

**Success Criteria:**
- [ ] All 5 charts created
- [ ] Charts are publication-quality
- [ ] Explanations are clear and insightful
- [ ] HTML report generated
- [ ] Report is readable and professional
- [ ] Insights are actionable

---

## 🔗 Navigation

**[← Back to Day 3 Module](./Day-3-Data-Visualization.md)** | **[Chapter 2 →](../README.md)**
