# Day 4: Embeddings & Similarity Computation

**Date:** Week 1, Day 4 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

✅ Understand one-hot vector representation
✅ Build co-occurrence matrices from text
✅ Calculate dot products between vectors
✅ Normalize vectors for comparison
✅ Implement cosine similarity from scratch
✅ Find similar words based on embeddings

---

## 📖 Core Topics

### 1. One-Hot Vector Representation

```python
def one_hot_encoding(word, vocab_size, word_to_index):
    """Create one-hot vector for word"""
    vector = [0] * vocab_size
    index = word_to_index.get(word)
    if index is not None:
        vector[index] = 1
    return vector

# Example
vocab = {'apple': 0, 'banana': 1, 'cherry': 2}
vocab_size = len(vocab)
v_apple = one_hot_encoding('apple', vocab_size, vocab)
# Output: [1, 0, 0]
```

### 2. Co-occurrence Matrices

```python
def build_cooccurrence_matrix(tokens, window_size=2, vocab_size=100, word_to_index=None):
    """Build word co-occurrence matrix"""
    matrix = [[0] * vocab_size for _ in range(vocab_size)]
    
    for i, word in enumerate(tokens):
        if word not in word_to_index:
            continue
        
        word_idx = word_to_index[word]
        
        # Context window (words before and after)
        start = max(0, i - window_size)
        end = min(len(tokens), i + window_size + 1)
        
        for j in range(start, end):
            if j != i and tokens[j] in word_to_index:
                context_idx = word_to_index[tokens[j]]
                matrix[word_idx][context_idx] += 1
    
    return matrix
```

### 3. Vector Operations

```python
import math

def dot_product(v1, v2):
    """Calculate dot product of two vectors"""
    return sum(x * y for x, y in zip(v1, v2))

def vector_magnitude(v):
    """Calculate magnitude (length) of vector"""
    return math.sqrt(sum(x ** 2 for x in v))

def normalize_vector(v):
    """Normalize vector to unit length"""
    mag = vector_magnitude(v)
    return [x / mag for x in v] if mag > 0 else v

def cosine_similarity(v1, v2):
    """Calculate cosine similarity between vectors"""
    # Method 1: Using normalized vectors
    v1_norm = normalize_vector(v1)
    v2_norm = normalize_vector(v2)
    return dot_product(v1_norm, v2_norm)
    
    # Method 2: Direct formula
    # dot = dot_product(v1, v2)
    # mag1 = vector_magnitude(v1)
    # mag2 = vector_magnitude(v2)
    # return dot / (mag1 * mag2) if mag1 * mag2 > 0 else 0
```

### 4. Finding Similar Words

```python
def find_similar_words(target_word, embeddings, word_to_index, k=3):
    """Find k most similar words to target"""
    if target_word not in word_to_index:
        return []
    
    target_idx = word_to_index[target_word]
    target_vector = embeddings[target_idx]
    
    similarities = []
    for i, word in enumerate(word_to_index.keys()):
        if word == target_word:
            continue
        
        similarity = cosine_similarity(target_vector, embeddings[i])
        similarities.append((word, similarity))
    
    # Sort by similarity descending
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:k]
```

### 5. Complete Embedding Engine

```python
class EmbeddingEngine:
    """Generate embeddings and compute similarities"""
    
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.embeddings = None
    
    def build_embeddings_from_cooccurrence(self, tokens, window_size=2):
        """Build embeddings from co-occurrence matrix"""
        vocab_size = self.vocabulary.size()
        
        # Build co-occurrence matrix
        cooccurrence = build_cooccurrence_matrix(
            tokens, window_size, vocab_size, 
            self.vocabulary.word_to_index
        )
        
        self.embeddings = cooccurrence
        return self.embeddings
    
    def get_embedding(self, word):
        """Get embedding vector for word"""
        if word not in self.vocabulary.word_to_index:
            return None
        
        idx = self.vocabulary.word_to_index[word]
        return self.embeddings[idx] if self.embeddings else None
    
    def similarity(self, word1, word2):
        """Compute similarity between two words"""
        v1 = self.get_embedding(word1)
        v2 = self.get_embedding(word2)
        
        if v1 is None or v2 is None:
            return 0
        
        return cosine_similarity(v1, v2)
    
    def find_similar(self, word, k=3):
        """Find k most similar words"""
        if word not in self.vocabulary.word_to_index:
            return []
        
        word_idx = self.vocabulary.word_to_index[word]
        target_vector = self.embeddings[word_idx]
        
        similarities = []
        for other_word, other_idx in self.vocabulary.word_to_index.items():
            if other_word == word:
                continue
            
            other_vector = self.embeddings[other_idx]
            sim = cosine_similarity(target_vector, other_vector)
            similarities.append((other_word, sim))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]
```

---

**[← Back to Chapter 1](./README.md)** | **[Day 4 Exercises →](./Day-4-Exercises.md)**
