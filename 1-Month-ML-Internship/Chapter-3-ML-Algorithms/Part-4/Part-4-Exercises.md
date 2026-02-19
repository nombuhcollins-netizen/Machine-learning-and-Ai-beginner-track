# Part 4: PCA - Exercises

**Difficulty:** Intermediate | **Time:** 6-7 hours | **Capstone:** Data Compressor

---

## 📝 Exercise Set 1: Variance and Covariance

### Exercise 1.1: Calculate Variance
Create a function that computes variance for each feature in a dataset.

**File:** `variance_calculation.py`

---

### Exercise 1.2: Covariance Matrix
Build function to compute covariance matrix:
- Should capture how features vary together
- Visualize as heatmap

**File:** `covariance_matrix.py`

---

### Exercise 1.3: Data Standardization
Create function to standardize data before PCA:
- Subtract mean
- Divide by standard deviation
- Essential for PCA to work properly

**File:** `standardize_data.py`

---

## 📝 Exercise Set 2: Eigenvalues & Eigenvectors

### Exercise 2.1: Compute Eigendecomposition
Implement eigendecomposition of covariance matrix:
- Use `np.linalg.eig()`
- Sort by eigenvalue (largest first)
- Interpret results

**File:** `eigendecomposition.py`

---

### Exercise 2.2: Eigenvector Interpretation
Visualize eigenvectors:
- Show direction of maximum variance
- Plot as arrows on scatter plot
- Explain what each represents

**File:** `eigenvector_visualization.py`

---

### Exercise 2.3: Explained Variance
Calculate how much variance each component explains:
- Divide eigenvalue by total variance
- Compute cumulative explained variance
- Determine components needed for 95% variance

**File:** `explained_variance.py`

---

## 📝 Exercise Set 3: PCA Implementation

### Exercise 3.1: SimplePCA Class
Implement PCA from scratch:
- `fit(X)` - learn components
- `transform(X)` - project data
- `fit_transform(X)` - both
- `explained_variance_ratio()` - returns ratios

**File:** `simple_pca.py`

---

### Exercise 3.2: Inverse Transform
Extend PCA to reconstruct original data:
- `inverse_transform(X_transformed)` - go back to original space
- Calculate reconstruction error
- Show how error increases with fewer components

**File:** `pca_inverse_transform.py`

---

### Exercise 3.3: Automatic Component Selection
Create function that selects # of components automatically:
- Input: target variance (e.g., 0.95)
- Output: minimum # of components needed
- Useful for dimensionality reduction

**File:** `auto_component_selection.py`

---

## 📝 Exercise Set 4: Visualization

### Exercise 4.1: Scree Plot
Create scree plot showing variance explained:
- X-axis: Principal component number
- Y-axis: % variance explained
- Show "elbow" where additional components don't help much

**File:** `scree_plot.py`

---

### Exercise 4.2: Cumulative Variance Plot
Plot cumulative explained variance:
- Show how many components needed for 95% threshold
- Useful for deciding dimensionality reduction level

**File:** `cumulative_variance_plot.py`

---

### Exercise 4.3: 2D Projections
Project high-D data to 2D using PCA:
- Visualize with scatter plot
- Color by class/category if available
- Show PC1 and PC2 variance percentages on axes

**File:** `pca_2d_projection.py`

---

## 📝 Exercise Set 5: Applications

### Exercise 5.1: Feature Extraction
Use PCA for feature extraction:
- Reduce feature space before ML model
- Train classifier on PCA components
- Compare with original features

**File:** `pca_feature_extraction.py`

---

### Exercise 5.2: Anomaly Detection
Use PCA for anomaly detection:
- Train on normal data
- Detect anomalies by reconstruction error
- Find data points that don't fit the learned components

**File:** `pca_anomaly_detection.py`

---

### Exercise 5.3: Noise Reduction
Use PCA to denoise data:
- Project to reduced space (removes noise)
- Reconstruct back to original space
- Show before/after denoising

**File:** `pca_denoising.py`

---

## 🎯 Capstone: Data Compressor

### Project: Reduce High-D Dataset to 2D

**Scenario:**
You're given a dataset with 20+ features and need to visualize it.

**Deliverables:**

#### Part 1: Load and Explore (`part1_explore.py`)
- Load dataset
- Check shape and stats
- Visualize (can't easily show 20D!)

#### Part 2: Apply PCA (`part2_apply_pca.py`)
```python
pca = SimplePCA(n_components=2)
X_2d = pca.fit_transform(X)

# Report
print(f"Reduced from {X.shape[1]} to {X_2d.shape[1]} dimensions")
print(f"Variance retained: {np.sum(pca.explained_variance_ratio()):.1%}")
```

#### Part 3: Visualize (`part3_visualize.py`)
- Scatter plot of 2D projection
- Color by class/category
- Add axes labels with variance %
- Show scree plot

#### Part 4: Analyze Components (`part4_analyze.py`)
- Which original features contribute to PC1?
- Which to PC2?
- Create loadings heatmap

#### Part 5: Compression Report (`part5_report.py`)
Output report:
```
PCA COMPRESSION REPORT
======================
Original: 20 dimensions × 1000 samples
Compressed: 2 dimensions × 1000 samples

Compression Ratio: 10x reduction

Variance Explained:
- PC1: 45.2%
- PC2: 23.8%
- Total: 69.0%

Benefits:
- Can now visualize data in 2D
- Fast computation (2 features instead of 20)
- Noise reduction

Trade-offs:
- Lost 31% of variance
- Some interpretability lost
- Specific features become PCs
```

**Success Criteria:**
- [ ] PCA implemented correctly
- [ ] At least 95% of original variance captured
- [ ] 2D projection is meaningful/interpretable
- [ ] Scree plot generated
- [ ] Report explains findings
- [ ] Code is well-documented

---

## 🔗 Navigation

**[← Back to Part 4 Module](./Part-4-Dimensionality-Reduction.md)** | **[Chapter 3 →](../README.md)**
