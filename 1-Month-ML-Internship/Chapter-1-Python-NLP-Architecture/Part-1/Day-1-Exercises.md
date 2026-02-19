# Day 1: Exercises - Advanced Python Data Structures & Functions

**Date:** Week 1, Day 1 | **Estimated Time:** 3-4 hours | **Difficulty:** Foundational

---

## Exercise Overview

These exercises reinforce list comprehensions, lambda functions, dictionaries, and math operations. Complete each exercise and commit your work to Git.

---

## Exercise 1: Master List Comprehensions

**Objective:** Develop fluency with list comprehension syntax and patterns

### 1.1 Basic Comprehensions

Create a Python script `exercise1_list_comprehensions.py`:

```python
# Exercise 1.1: Create a list of squares for numbers 1-20
# TODO: Use list comprehension

# Exercise 1.2: Filter even numbers from 0-50
# TODO: Use list comprehension with condition

# Exercise 1.3: Convert list of words to uppercase
words = ["python", "data", "science", "machine", "learning"]
# TODO: Use list comprehension

# Exercise 1.4: Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# TODO: Use nested list comprehension

# Exercise 1.5: Create pairs of (number, square, cube)
# TODO: Use list comprehension for numbers 1-10
```

**Expected Output:**
```
Exercise 1.1 result: [1, 4, 9, 16, 25, ...]
Exercise 1.2 result: [0, 2, 4, 6, 8, ...]
Exercise 1.3 result: ['PYTHON', 'DATA', 'SCIENCE', ...]
Exercise 1.4 result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Exercise 1.5 result: [(1, 1, 1), (2, 4, 8), ...]
```

**Verification Checklist:**
- [ ] All 5 comprehensions implemented
- [ ] Code uses only list comprehension (no explicit loops)
- [ ] Correct results printed
- [ ] File saved as `exercise1_list_comprehensions.py`

---

## Exercise 2: Dictionary Operations for Text

**Objective:** Build frequency counting and indexing systems

Create a Python script `exercise2_dict_operations.py`:

```python
# Exercise 2.1: Count word frequencies in a sentence
text = "the quick brown fox jumps over the lazy dog the fox is quick"
# TODO: Create dict with word frequencies using dict comprehension

# Exercise 2.2: Create word-to-index mapping
# From exercise 2.1 frequencies, create bidirectional mapping
# TODO: word_to_index and index_to_word dictionaries

# Exercise 2.3: Sort frequencies by count (descending)
# TODO: Return list of tuples (word, count) sorted by count

# Exercise 2.4: Top N words
# TODO: Function to return top N most frequent words

# Exercise 2.5: Merge multiple word frequency dictionaries
freq_dict1 = {'apple': 3, 'banana': 2}
freq_dict2 = {'apple': 1, 'cherry': 4}
freq_dict3 = {'banana': 1, 'date': 2}
# TODO: Merge all three dicts accumulating counts
```

**Expected Output:**
```
Exercise 2.1: {'the': 3, 'quick': 2, 'brown': 1, ...}
Exercise 2.2: word_to_index: {...}, index_to_word: {...}
Exercise 2.3: [('the', 3), ('quick', 2), ('fox', 2), ...]
Exercise 2.4 (top 3): [('the', 3), ('quick', 2), ('fox', 2)]
Exercise 2.5: {'apple': 4, 'banana': 3, 'cherry': 4, 'date': 2}
```

**Verification Checklist:**
- [ ] Frequencies calculated correctly
- [ ] Bidirectional mappings work correctly
- [ ] Sorting by count is descending
- [ ] Top N function works for different N values
- [ ] Merging accumulates counts properly

---

## Exercise 3: Lambda Functions & Functional Programming

**Objective:** Use lambdas for filtering, mapping, and sorting

Create a Python script `exercise3_lambda_functions.py`:

```python
# Exercise 3.1: Filter words longer than 3 characters
words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
# TODO: Use filter() with lambda

# Exercise 3.2: Transform (double) all numbers in a list
numbers = [1, 2, 3, 4, 5]
# TODO: Use map() with lambda

# Exercise 3.3: Sort students by grade (descending), then by name
students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 85),
    ('David', 78),
    ('Eve', 92)
]
# TODO: Sort using lambda key

# Exercise 3.4: Filter and transform in one step
# From numbers list, keep only odd numbers and cube them
# TODO: Combine filter() and map() using lambdas

# Exercise 3.5: Sum with condition using reduce
# Calculate sum of squares for even numbers only
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Use reduce() with lambda (may need filter first)
```

**Expected Output:**
```
Exercise 3.1: ['quick', 'brown', 'jumps', 'over']
Exercise 3.2: [2, 4, 6, 8, 10]
Exercise 3.3: [('Eve', 92), ('Bob', 92), ('Alice', 85), ('Charlie', 85), ('David', 78)]
Exercise 3.4: [1, 27, 125, 343, 729]
Exercise 3.5: 220 (4 + 16 + 36 + 64 + 100)
```

**Verification Checklist:**
- [ ] Filter works correctly
- [ ] Map transforms all elements
- [ ] Sort uses multiple criteria correctly
- [ ] Combined filter/map works
- [ ] Reduce calculates correct sum

---

## Exercise 4: Math Module Operations

**Objective:** Implement vector operations for text embeddings

Create a Python script `exercise4_math_operations.py`:

```python
import math
from functools import reduce

# Exercise 4.1: Implement dot product
# Inputs: v1 = [1, 2, 3], v2 = [4, 5, 6]
# TODO: Function dot_product(v1, v2) returning 32

# Exercise 4.2: Implement vector magnitude
# Input: v = [3, 4]
# TODO: Function vector_magnitude(v) returning 5.0

# Exercise 4.3: Implement cosine similarity
# Two vectors: v1, v2
# TODO: cosine_similarity(v1, v2) returning similarity score

# Exercise 4.4: Normalize a vector
# Input: v = [3, 4]
# TODO: normalize(v) returning [0.6, 0.8]

# Exercise 4.5: Calculate statistics using math module
scores = [78, 85, 92, 88, 76, 95, 89]
# TODO: mean, median (for odd list), variance, std_dev using math functions
```

**Expected Output:**
```
Exercise 4.1 (dot product): 32
Exercise 4.2 (magnitude): 5.0
Exercise 4.3 (cosine sim): 0.9746 (for [1,2,3] & [4,5,6])
Exercise 4.4 (normalize): [0.6, 0.8]
Exercise 4.5: mean=87.0, median=89, variance=45.14, std_dev=6.72
```

**Verification Checklist:**
- [ ] Dot product calculation correct
- [ ] Vector magnitude uses sqrt correctly
- [ ] Cosine similarity between 0 and 1
- [ ] Normalization produces unit vector
- [ ] Statistics calculated accurately

---

## Exercise 5: Edge Case Handling

**Objective:** Handle encoding errors and text anomalies

Create a Python script `exercise5_edge_cases.py`:

```python
# Exercise 5.1: Clean mixed whitespace
text_with_whitespace = "Hello   \n\n  World  \r\n  Python  \t\t!"
# TODO: clean_whitespace(text) returning normalized text

# Exercise 5.2: Handle unicode characters
text_unicode = "café schöne naïve résumé"
# TODO: remove_accents(text) returning ASCII equivalent
# Hint: Use encode/decode with 'ignore'

# Exercise 5.3: Safe file reading with encoding fallback
# TODO: Function read_text_safe(filepath, encoding='utf-8')
# Try: utf-8, latin-1, cp1252 before failing

# Exercise 5.4: Handle division by zero
# Vector magnitude could be 0
# TODO: safe_cosine_similarity(v1, v2) handling zero case

# Exercise 5.5: Handle empty/None inputs
texts = ["hello", "", None, "world", ""]
# TODO: filter_valid(texts) returning only non-empty strings
```

**Expected Output:**
```
Exercise 5.1: "Hello World Python !"
Exercise 5.2: "cafe schone naive resume"
Exercise 5.3: Successfully reads file with fallback encoding
Exercise 5.4: Returns 0 if magnitude is 0
Exercise 5.5: ['hello', 'world']
```

**Verification Checklist:**
- [ ] Whitespace normalized correctly
- [ ] Unicode removed to ASCII
- [ ] File reading handles multiple encodings
- [ ] Division by zero handled gracefully
- [ ] Empty/None values filtered correctly

---

## Exercise 6: Capstone - Word Frequency Engine

**Objective:** Combine all Day 1 concepts into a complete tool

Create a Python script `exercise6_word_frequency_engine.py`:

```python
import json
import math
from functools import reduce
from collections import defaultdict

class WordFrequencyEngine:
    """
    Advanced word frequency analyzer combining all Day 1 concepts.
    """
    
    def __init__(self, min_word_length=2):
        self.min_word_length = min_word_length
        self.vocabularies = {}  # Multiple vocabularies for multiple files
    
    # TODO: Implement methods:
    # - analyze_text(text) -> dict of frequencies
    # - top_n_words(n=10) -> list of top N words
    # - get_statistics() -> dict with min, max, avg frequency
    # - save_to_json(filepath) -> export vocabularies
    # - process_multiple_files(file_list) -> analyze all files
    
    def clean_text(self, text):
        """Clean text: normalize whitespace, handle encoding"""
        # TODO: Implement text cleaning
        pass
    
    def tokenize(self, text):
        """Tokenize and filter by minimum length"""
        # TODO: Implement tokenization with filtering
        pass
    
    def count_frequencies(self, words):
        """Count word frequencies"""
        # TODO: Implement using dict comprehension or .get()
        pass
    
    def calculate_statistics(self):
        """Calculate min, max, mean frequency"""
        # TODO: Implement using math.ceil, math.floor, reduce
        pass

# Usage Example:
# engine = WordFrequencyEngine(min_word_length=3)
# engine.process_multiple_files(['file1.txt', 'file2.txt', 'file3.txt'])
# top_words = engine.top_n_words(n=20)
# stats = engine.get_statistics()
# print(f"Analyzed {len(engine.vocabularies)} files")
# print(f"Top 20 words: {top_words}")
# print(f"Statistics: {stats}")
```

**Expected Functionality:**
- Loads multiple text files
- Cleans and tokenizes text
- Creates frequency dictionaries
- Ranks and filters results
- Exports to JSON format

**Verification Checklist:**
- [ ] Reads files without encoding errors
- [ ] Tokenizes text correctly
- [ ] Counts frequencies accurately
- [ ] Calculates statistics correctly
- [ ] Exports valid JSON
- [ ] Class is well-documented
- [ ] All methods implemented

---

## Commit Strategy

After completing each exercise section:

```bash
# After Exercise 1
git add exercise1_list_comprehensions.py
git commit -m "feat: Complete Day 1 Exercise 1 - List Comprehensions"

# After Exercise 2
git add exercise2_dict_operations.py
git commit -m "feat: Complete Day 1 Exercise 2 - Dictionary Operations"

# After Exercise 3
git add exercise3_lambda_functions.py
git commit -m "feat: Complete Day 1 Exercise 3 - Lambda Functions"

# After Exercise 4
git add exercise4_math_operations.py
git commit -m "feat: Complete Day 1 Exercise 4 - Math Operations"

# After Exercise 5
git add exercise5_edge_cases.py
git commit -m "feat: Complete Day 1 Exercise 5 - Edge Case Handling"

# After Capstone
git add exercise6_word_frequency_engine.py
git commit -m "feat: Complete Day 1 Exercise 6 - Word Frequency Engine (Capstone)"
```

---

## Self-Assessment

Before moving to Day 2, verify:

✅ All exercises completed without errors
✅ List comprehensions preferred over loops
✅ Lambda functions used appropriately
✅ Dictionaries handle frequencies correctly
✅ Math operations produce accurate results
✅ Edge cases handled gracefully
✅ Code is readable with clear variable names
✅ Functions have docstrings
✅ All commits made to Git

---

## 🔗 Navigation

**[← Back to Day 1 Module](./Day-1-Advanced-Python.md)** | **[Day 2 Module →](./Day-2-Text-Preprocessing.md)**
