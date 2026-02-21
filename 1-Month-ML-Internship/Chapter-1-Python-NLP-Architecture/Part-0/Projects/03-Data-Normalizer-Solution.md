# Project 3 Solution: ML Data Normalizer

\`\`\`python
import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def normalize_minmax(values):
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    return [(v - min_val) / range_val if range_val != 0 else 0 for v in values]

def process_data(filename, output_train, output_test):
    # Read data
    data = read_csv(filename)
    
    # Extract features and labels
    features = []
    labels = []
    for row in data:
        features.append([float(row['age']), float(row['salary'])])
        labels.append(int(row['promotion']))
    
    # Normalize
    norm_features = []
    for i in range(len(features[0])):
        col = [f[i] for f in features]
        norm_col = normalize_minmax(col)
        norm_features.append(norm_col)
    
    # Transpose
    norm_data = [[norm_features[j][i] for j in range(len(norm_features))] 
                 for i in range(len(features))]
    
    # Split and save
    split = int(0.8 * len(norm_data))
    # ... save train and test sets
\`\`\`

---
