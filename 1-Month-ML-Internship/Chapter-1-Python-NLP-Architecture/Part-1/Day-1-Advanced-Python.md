# Day 1: Advanced Python Data Structures & Functions

**Date:** Week 1, Day 1 | **Duration:** 7+ Hours | **Difficulty:** Foundational

---

## 🎯 Learning Objectives

By the end of Day 1, you will:

✅ Master list comprehensions for efficient data manipulation
✅ Understand lambda functions and functional programming in Python
✅ Work with dictionaries for counting and frequency analysis
✅ Use the math module for numerical operations
✅ Handle encoding errors and edge cases in text data
✅ Build the foundation for text processing pipelines

---

## 📖 Core Topics

### 1. Advanced List Operations

#### List Comprehensions
**Concept:** Create new lists by filtering, transforming, or combining existing lists in a single line.

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested comprehension (flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With transformation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# Output: ['HELLO', 'WORLD', 'PYTHON']
```

**Why It Matters:**
- More readable than loops
- Faster execution
- Functional programming approach
- Reduces code lines

#### Nested List Comprehensions
```python
# Creating a matrix
matrix = [[0 for _ in range(3)] for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Conditional with nested structure
data = [1, 2, 3, 4, 5]
result = [[x, x**2] for x in data if x > 2]
# [[3, 9], [4, 16], [5, 25]]
```

---

### 2. Dictionary Operations for Text Processing

#### Basic Dictionary Operations
```python
# Creating a frequency dictionary
text = "hello world hello python world world"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
# Output: {'hello': 2, 'world': 3, 'python': 1}

# Dictionary comprehension
freq = {word: words.count(word) for word in set(words)}
# Output: {'hello': 2, 'world': 3, 'python': 1}
```

#### Sorting and Ranking
```python
# Sort by value (frequency)
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# Output: [('world', 3), ('hello', 2), ('python', 1)]

# Top N words
top_3 = dict(sorted_freq[:3])
# Output: {'world': 3, 'hello': 2, 'python': 1}

# Get top N values only
top_values = [count for word, count in sorted_freq[:3]]
# Output: [3, 2, 1]
```

#### Dictionary Merging and Conversion
```python
# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Creating inverted index
word_to_index = {'apple': 0, 'banana': 1, 'cherry': 2}
index_to_word = {v: k for k, v in word_to_index.items()}
# Output: {0: 'apple', 1: 'banana', 2: 'cherry'}
```

---

### 3. Lambda Functions & Functional Programming

#### Lambda Basics
```python
# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# In filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Output: [2, 4, 6, 8, 10]

# In map()
doubled = list(map(lambda x: x * 2, numbers))
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

#### Lambda with Multiple Arguments
```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Sorting by multiple criteria
data = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
# Output: [('Bob', 20), ('Alice', 25), ('Charlie', 25)]
```

#### Functional Composition
```python
# Combining operations
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x > 2, data)))
# Output: [9, 16, 25]

# Using reduce() for aggregation
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# Output: 120
```

---

### 4. Math Module Operations

#### Basic Math Functions
```python
import math

# Common functions
x = 16
print(math.sqrt(x))      # 4.0
print(math.factorial(5)) # 120
print(math.log(100))     # 4.605 (natural log)
print(math.log10(100))   # 2.0 (base 10 log)
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
```

#### Vector Math (for embeddings)
```python
import math

def dot_product(v1, v2):
    """Calculate dot product of two vectors"""
    return sum(x * y for x, y in zip(v1, v2))

def vector_magnitude(v):
    """Calculate the magnitude (length) of a vector"""
    return math.sqrt(sum(x ** 2 for x in v))

# Example
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(dot_product(v1, v2))      # 32
print(vector_magnitude(v1))      # 3.74...

# Cosine similarity (preview for Day 4)
def cosine_similarity(v1, v2):
    """Calculate cosine similarity between two vectors"""
    dot = dot_product(v1, v2)
    mag1 = vector_magnitude(v1)
    mag2 = vector_magnitude(v2)
    return dot / (mag1 * mag2) if mag1 * mag2 != 0 else 0

similarity = cosine_similarity(v1, v2)
print(f"Similarity: {similarity:.4f}")  # 0.9746
```

---

### 5. Handling Text Edge Cases

#### Encoding Issues
```python
# Problem: Mixed encodings in text
text = "Hello\nWorld\r\nPython\t\t!"

# Solution: Normalize whitespace
def clean_whitespace(text):
    """Remove extra whitespace and line breaks"""
    return ' '.join(text.split())

cleaned = clean_whitespace(text)
# Output: "Hello World Python !"

# Handling unicode
text_with_unicode = "café résumé naïve"
normalized = text_with_unicode.encode('ascii', 'ignore').decode('ascii')
# Output: "cafe resume naive"
```

#### File Reading with Encoding Handling
```python
def read_text_safe(filepath, encoding='utf-8'):
    """Read text file with fallback encoding"""
    encodings = [encoding, 'utf-8', 'latin-1', 'cp1252']
    
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    
    raise ValueError(f"Could not read {filepath} with any encoding")

# Usage
text = read_text_safe('document.txt')
```

---

## 🔗 Connecting Concepts

```
Data Structures (Lists, Dicts)
    ↓
List Comprehensions (Efficient creation)
    ↓
Lambda Functions (Functional operations)
    ↓
Dictionary Operations (Counting frequencies)
    ↓
Math Module (Numerical calculations)
    ↓
Edge Case Handling (Robust code)
    ↓
Ready for text processing!
```

---

## 💡 Practical Example: Word Frequency Analyzer

```python
import math
from functools import reduce
from collections import defaultdict

def analyze_words(text):
    """Complete Day 1 example combining all concepts"""
    
    # Step 1: Clean text
    text = ' '.join(text.split())
    
    # Step 2: Tokenize
    words = text.lower().split()
    
    # Step 3: Filter and count
    filtered = [w for w in words if len(w) > 2]
    
    # Step 4: Create frequency dictionary
    freq = {word: filtered.count(word) for word in set(filtered)}
    
    # Step 5: Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Step 6: Calculate statistics using math
    total = reduce(lambda x, y: x + y, freq.values())
    average = total / len(freq) if freq else 0
    
    return {
        'frequencies': sorted_freq,
        'total_words': total,
        'unique_words': len(freq),
        'average_frequency': average
    }

# Usage
text = "Python is great Python is fun Python is powerful"
result = analyze_words(text)
print(result)
# Output:
# {
#     'frequencies': [('python', 3), ('great', 1), ('powerful', 1)],
#     'total_words': 5,
#     'unique_words': 3,
#     'average_frequency': 1.67
# }
```

---

## 🎯 Key Takeaways

1. **List comprehensions** are more Pythonic than loops
2. **Dictionaries** are perfect for frequency counting
3. **Lambda functions** enable functional programming style
4. **Math module** provides essential numerical operations
5. **Edge case handling** makes code robust and production-ready
6. Combine these concepts for powerful text processing

---

## 🔗 Navigation

**[← Back to Chapter 1](./README.md)** | **[Day 1 Exercises →](./Day-1-Exercises.md)**
