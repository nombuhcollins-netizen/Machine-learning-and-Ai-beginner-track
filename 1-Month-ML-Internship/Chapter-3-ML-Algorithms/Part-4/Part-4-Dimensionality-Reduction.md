# Part 4: Principal Component Analysis (PCA)

**Week:** Week 3, Part 4 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

By the end of Part 4, you will:

✅ Understand variance and covariance matrices
✅ Calculate eigenvalues and eigenvectors geometrically
✅ Implement PCA from scratch
✅ Reduce high-dimensional data while preserving variance
✅ Visualize high-dimensional data in 2D/3D
✅ Explain variance explained by principal components
✅ Apply PCA for feature extraction and visualization

---

## 📖 Core Topics

### 1. Variance and Covariance in High Dimensions

#### Understanding Variance
```python
import numpy as np

# Dataset with 2 features
data = np.array([
    [1, 2],
    [2, 4],
    [3, 5],
    [4, 7],
    [5, 8]
])

# Variance of each feature
var_feature1 = np.var(data[:, 0])  # Variance of X
var_feature2 = np.var(data[:, 1])  # Variance of Y

print(f"Variance X: {var_feature1:.2f}")
print(f"Variance Y: {var_feature2:.2f}")
```

#### Covariance Matrix
```python
# Covariance captures how features vary together
cov_matrix = np.cov(data.T)

# Output: [[var_x,    cov_xy],
#          [cov_yx,   var_y]]

print("Covariance Matrix:")
print(cov_matrix)
```

---

### 2. Eigenvalues and Eigenvectors

#### Computing Eigendecomposition
```python
# Eigenvalues and eigenvectors of covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort by eigenvalue (largest first)
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
```

#### Interpretation
- **Eigenvalues:** Variance along each principal component
- **Eigenvectors:** Direction of maximum variance

---

### 3. PCA Implementation from Scratch

#### Manual PCA
```python
class SimplePCA:
    """PCA implemented from scratch"""
    
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.mean = None
        self.components = None
        self.explained_variance = None
    
    def fit(self, X):
        """Fit PCA to data"""
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # Compute covariance matrix
        cov_matrix = np.cov(X_centered.T)
        
        # Eigendecomposition
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        
        # Sort by eigenvalue
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # Store components
        self.components = eigenvectors[:, :self.n_components]
        self.explained_variance = eigenvalues[:self.n_components]
        
        return self
    
    def transform(self, X):
        """Project data onto principal components"""
        X_centered = X - self.mean
        return X_centered @ self.components
    
    def fit_transform(self, X):
        return self.fit(X).transform(X)
    
    def explained_variance_ratio(self):
        """Fraction of variance explained"""
        total_var = np.sum(self.explained_variance)
        return self.explained_variance / total_var
    
    def inverse_transform(self, X_transformed):
        """Reconstruct from principal components"""
        return X_transformed @ self.components.T + self.mean

# Usage
pca = SimplePCA(n_components=2)
X_reduced = pca.fit_transform(data)
print(f"Reduced shape: {X_reduced.shape}")  # (n_samples, 2)

# Explained variance
explained = pca.explained_variance_ratio()
print(f"Explained variance: {explained}")  # [0.XX, 0.XX]
```

---

### 4. Visualization and Interpretation

#### Scree Plot
```python
import matplotlib.pyplot as plt

# Variance explained by each component
variance_explained = pca.explained_variance_ratio()
cumulative_variance = np.cumsum(variance_explained)

plt.figure(figsize=(10, 4))

# Scree plot
plt.subplot(1, 2, 1)
plt.plot(range(1, len(variance_explained) + 1), variance_explained, 'bo-')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.title('Scree Plot')

# Cumulative variance
plt.subplot(1, 2, 2)
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, 'go-')
plt.axhline(0.95, color='r', linestyle='--', label='95% threshold')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Variance Explained')
plt.title('Cumulative Explained Variance')
plt.legend()

plt.tight_layout()
plt.show()
```

#### Visualization in 2D
```python
# Project high-dimensional data to 2D
pca_2d = SimplePCA(n_components=2)
X_pca = pca_2d.fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel(f'PC1 ({pca_2d.explained_variance_ratio()[0]:.1%} variance)')
plt.ylabel(f'PC2 ({pca_2d.explained_variance_ratio()[1]:.1%} variance)')
plt.title('PCA Projection')
plt.show()
```

---

### 5. Handling High-Dimensional Data

#### Dimensionality Reduction Pipeline
```python
class DimensionalityReducer:
    """Reduce high-D data while preserving structure"""
    
    def __init__(self, variance_threshold=0.95):
        self.variance_threshold = variance_threshold
        self.n_components = None
        self.pca = None
    
    def fit(self, X):
        """Find # components needed for threshold"""
        # Fit full PCA
        pca_full = SimplePCA(n_components=X.shape[1])
        pca_full.fit(X)
        
        # Find components needed
        cum_var = np.cumsum(pca_full.explained_variance_ratio())
        self.n_components = np.argmax(cum_var >= self.variance_threshold) + 1
        
        # Fit reduced PCA
        self.pca = SimplePCA(n_components=self.n_components)
        self.pca.fit(X)
        
        return self
    
    def transform(self, X):
        return self.pca.transform(X)
    
    def fit_transform(self, X):
        return self.fit(X).transform(X)
    
    def reconstruction_error(self, X):
        """Measure quality of compression"""
        X_transformed = self.transform(X)
        X_reconstructed = self.pca.inverse_transform(X_transformed)
        error = np.mean((X - X_reconstructed) ** 2)
        return error

# Usage
reducer = DimensionalityReducer(variance_threshold=0.95)
X_compressed = reducer.fit_transform(X)
print(f"Reduced from {X.shape[1]} to {reducer.n_components} dimensions")
print(f"Reconstruction error: {reducer.reconstruction_error(X):.4f}")
```

---

## 💡 Complete Example: Data Compression

```python
class DataCompressor:
    """Compress high-D data for visualization"""
    
    def __init__(self, target_dims=2):
        self.target_dims = target_dims
        self.reducer = None
        self.original_shape = None
    
    def compress(self, X):
        """Compress to target dimensions"""
        self.original_shape = X.shape
        
        # Reduce to 2D for visualization
        self.reducer = SimplePCA(n_components=self.target_dims)
        X_compressed = self.reducer.fit_transform(X)
        
        return X_compressed
    
    def compression_report(self, X):
        """Report on compression efficiency"""
        X_compressed = self.compress(X)
        
        report = {
            'original_dimensions': self.original_shape[1],
            'compressed_dimensions': X_compressed.shape[1],
            'compression_ratio': self.original_shape[1] / X_compressed.shape[1],
            'variance_retained': np.sum(self.reducer.explained_variance_ratio())
        }
        
        return report

# Usage
compressor = DataCompressor(target_dims=2)
X_2d = compressor.compress(X)
print(compressor.compression_report(X))
```

---

## 🔗 Navigation

**[← Back to Chapter 3](../README.md)** | **[Part 4 Exercises →](./Part-4-Exercises.md)**
