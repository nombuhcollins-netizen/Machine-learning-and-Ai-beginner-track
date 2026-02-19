# Day 4: Exercises - Embeddings & Similarity Computation

**Date:** Week 1, Day 4 | **Estimated Time:** 3-4 hours | **Difficulty:** Intermediate

---

## Exercise 1: Vector Operations

Create `exercise1_vector_operations.py`:

```python
import math

# Exercise 1.1: Implement dot_product()
v1 = [1, 2, 3]
v2 = [4, 5, 6]
# TODO: Calculate dot product (should be 32)

# Exercise 1.2: Implement vector_magnitude()
v = [3, 4]
# TODO: Calculate magnitude (should be 5.0)

# Exercise 1.3: Implement normalize_vector()
v = [3, 4]
# TODO: Normalize to unit vector (should be [0.6, 0.8])

# Exercise 1.4: Implement cosine_similarity()
v1 = [1, 2, 3]
v2 = [4, 5, 6]
# TODO: Calculate cosine similarity (should be ~0.97)

# Exercise 1.5: Test with one-hot vectors
vocab_size = 5
v1_onehot = [1, 0, 0, 0, 0]  # First word
v2_onehot = [0, 1, 0, 0, 0]  # Second word
# TODO: Compute similarity (should be 0, orthogonal)
```

---

## Exercise 2: One-Hot Encoding

Create `exercise2_onehot_encoding.py`:

```python
# Exercise 2.1: Implement one_hot_encoding()
vocab = {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}
# TODO: Generate one-hot for 'apple', 'banana', 'cherry'

# Exercise 2.2: Batch one-hot encoding
words = ['apple', 'banana', 'cherry', 'apple']
# TODO: Create one-hot matrix for all words

# Exercise 2.3: Verify orthogonality
# Different one-hot vectors should have similarity 0
# TODO: Test all pairs
```

---

## Exercise 3: Co-occurrence Matrices

Create `exercise3_cooccurrence.py`:

```python
# Exercise 3.1: Build co-occurrence matrix
tokens = ['the', 'cat', 'sat', 'on', 'the', 'mat']
vocab = {'the': 0, 'cat': 1, 'sat': 2, 'on': 3, 'mat': 4}
window_size = 2

# TODO: Build co-occurrence matrix
# TODO: Verify 'the' and 'cat' have non-zero co-occurrence

# Exercise 3.2: Analyze co-occurrence
# TODO: Find most co-occurring word pairs

# Exercise 3.3: Co-occurrence with larger corpus
text = "the dog and the cat sat with the dog"
tokens = text.split()
# TODO: Build and analyze co-occurrence matrix
```

---

## Exercise 4: EmbeddingEngine Class

Create `exercise4_embedding_engine.py`:

```python
class EmbeddingEngine:
    """Complete embedding system"""
    
    # TODO: Implement:
    # - __init__(vocabulary)
    # - build_embeddings_from_cooccurrence(tokens, window_size)  
    # - get_embedding(word)
    # - similarity(word1, word2)
    # - find_similar(word, k=3)

# Test with sample corpus
corpus = """
machine learning is a subset of artificial intelligence
deep learning uses neural networks
machine learning enables computers to learn"""

# TODO: 
# 1. Build vocabulary
# 2. Create embedding engine
# 3. Find similar words to 'learning', 'machine', 'deep'
```

---

## Exercise 5: Capstone - Mini Embedding Engine

Create `exercise5_mini_embedding_engine.py`:

```python
class MiniEmbeddingEngine:
    """Complete mini embedding system (Capstone)"""
    
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.vocabulary = DynamicVocabulary()
        self.embeddings = None
    
    # TODO: Implement all methods from Day 4 module
    
    def query_similar(self, word, k=3):
        """CLI-style query for similar words"""
        # TODO: Return formatted output with similarities

# Usage Example:
# engine = MiniEmbeddingEngine(tokenizer)
# corpus_tokens = [...process documents...]
# engine.build_embeddings(corpus_tokens)
# similar_words = engine.query_similar('machine', k=5)
# print_results(similar_words)
```

---

## Commit Strategy

```bash
git add exercise1_vector_operations.py
git commit -m "feat: Complete Day 4 Exercise 1 - Vector Operations"

git add exercise2_onehot_encoding.py
git commit -m "feat: Complete Day 4 Exercise 2 - One-Hot Encoding"

git add exercise3_cooccurrence.py
git commit -m "feat: Complete Day 4 Exercise 3 - Co-occurrence Matrices"

git add exercise4_embedding_engine.py
git commit -m "feat: Complete Day 4 Exercise 4 - EmbeddingEngine Class"

git add exercise5_mini_embedding_engine.py
git commit -m "feat: Complete Day 4 Exercise 5 - Mini Embedding Engine (Capstone)"
```

---

**[← Back to Day 4 Module](./Day-4-Embeddings-Similarity.md)** | **[Day 5 Module →](./Day-5-NLP-Integration.md)**
