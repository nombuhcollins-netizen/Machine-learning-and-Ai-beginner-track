# Day 4: Information Retrieval & Inverted Indexes

**Date:** Week 2, Day 4 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

By the end of Day 4, you will:

✅ Build term-incidence matrices from documents
✅ Construct inverted indexes for O(1) keyword lookup
✅ Implement boolean search queries (AND, OR, NOT)
✅ Optimize search performance with data structures
✅ Combine Day 1-3 knowledge for search systems
✅ Prepare for web-based search interface (Day 5)

---

## 📖 Core Topics

### 1. Term-Incidence Matrices

#### Basic Concept
```python
def build_term_incidence_matrix(documents):
    """Build matrix: documents × terms"""
    
    all_terms = set()
    for doc in documents:
        all_terms.update(doc.split())
    
    terms = sorted(list(all_terms))
    matrix = []
    
    for doc in documents:
        doc_terms = set(doc.split())
        row = [1 if term in doc_terms else 0 for term in terms]
        matrix.append(row)
    
    return np.array(matrix), terms

# Usage
documents = [
    "python programming language",
    "machine learning algorithms",
    "python machine learning"
]

matrix, terms = build_term_incidence_matrix(documents)
print("Matrix:")
print(matrix)
print("Terms:", terms)
```

---

### 2. Inverted Index Structure

#### Building Inverted Index
```python
class InvertedIndex:
    """Maps words to document IDs (O(1) lookup)"""
    
    def __init__(self):
        self.index = {}  # word -> [doc_ids]
        self.documents = {}  # id -> content
        self.doc_count = 0
    
    def add_document(self, content):
        """Add document to index"""
        doc_id = self.doc_count
        self.documents[doc_id] = content
        
        # Tokenize and index
        words = set(content.lower().split())
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(doc_id)
        
        self.doc_count += 1
        return doc_id
    
    def search(self, word):
        """Find documents containing word - O(1) lookup"""
        word = word.lower()
        return self.index.get(word, [])
    
    def get_document(self, doc_id):
        """Retrieve document by ID"""
        return self.documents.get(doc_id)

# Usage
index = InvertedIndex()
index.add_document("python programming tutorial")
index.add_document("machine learning with python")
index.add_document("data science in python")

# Search - O(1) lookup
results = index.search("python")
print(f"'python' found in documents: {results}")
```

---

### 3. Boolean Search Queries

#### AND, OR, NOT Operations
```python
class BooleanSearchEngine:
    """Boolean search on inverted index"""
    
    def __init__(self, index):
        self.index = index
    
    def search_and(self, *words):
        """Find docs containing ALL words"""
        if not words:
            return []
        
        result = set(self.index.search(words[0]))
        for word in words[1:]:
            result = result.intersection(set(self.index.search(word)))
        
        return sorted(list(result))
    
    def search_or(self, *words):
        """Find docs containing ANY word"""
        result = set()
        for word in words:
            result = result.union(set(self.index.search(word)))
        
        return sorted(list(result))
    
    def search_not(self, word):
        """Find docs NOT containing word"""
        all_docs = set(self.index.documents.keys())
        matching_docs = set(self.index.search(word))
        
        return sorted(list(all_docs - matching_docs))

# Usage
engine = BooleanSearchEngine(index)

# AND query
results = engine.search_and("python", "machine")
print(f"Docs with 'python' AND 'machine': {results}")

# OR query
results = engine.search_or("python", "data")
print(f"Docs with 'python' OR 'data': {results}")

# NOT query
results = engine.search_not("tutorial")
print(f"Docs WITHOUT 'tutorial': {results}")
```

---

### 4. Real-World Search Optimizations

#### Preprocessing for Better Search
```python
import re
import string

class PreprocessedInvertedIndex:
    """Inverted index with text preprocessing"""
    
    def __init__(self):
        self.index = {}
        self.documents = {}
        self.doc_count = 0
        self.stopwords = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to'
        }
    
    def preprocess(self, text):
        """Normalize text: lowercase, remove punct, stopwords"""
        # Lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Split and filter stopwords
        words = [w for w in text.split() if w not in self.stopwords and len(w) > 2]
        
        return words
    
    def add_document(self, content):
        """Add and preprocess document"""
        doc_id = self.doc_count
        self.documents[doc_id] = content
        
        words = set(self.preprocess(content))
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(doc_id)
        
        self.doc_count += 1
        return doc_id
    
    def search(self, query):
        """Search with preprocessing"""
        words = self.preprocess(query)
        
        # Find docs with ANY query word
        results = set()
        for word in words:
            results = results.union(set(self.index.get(word, [])))
        
        return sorted(list(results))

# Usage
index = PreprocessedInvertedIndex()
index.add_document("Python is a great programming language")
index.add_document("Data science uses machine learning")

results = index.search("python programming")
print(f"Results: {results}")
```

---

### 5. Ranking and Scoring

#### TF-IDF Scoring
```python
import math

class TFIDFSearchEngine:
    """Search with relevance scoring"""
    
    def __init__(self, index):
        self.index = index
        self.idf = {}
        self._compute_idf()
    
    def _compute_idf(self):
        """Compute IDF for each term"""
        total_docs = len(self.index.documents)
        
        for word, doc_ids in self.index.index.items():
            # IDF = log(total_docs / docs_with_term)
            self.idf[word] = math.log(total_docs / len(doc_ids))
    
    def _compute_tf(self, word, doc_id):
        """Compute TF for word in document"""
        doc_text = self.index.documents[doc_id]
        words = doc_text.lower().split()
        
        count = words.count(word.lower())
        return count / len(words) if words else 0
    
    def score_document(self, doc_id, query_words):
        """Score document for query"""
        score = 0
        for word in query_words:
            if word in self.index.index:
                tf = self._compute_tf(word, doc_id)
                idf = self.idf.get(word, 0)
                score += tf * idf
        
        return score
    
    def ranked_search(self, query):
        """Search and rank results"""
        query_words = query.lower().split()
        
        # Find docs containing any query word
        matching_docs = set()
        for word in query_words:
            matching_docs.update(self.index.search(word))
        
        # Score and rank
        scored = [(doc_id, self.score_document(doc_id, query_words)) 
                  for doc_id in matching_docs]
        scored.sort(key=lambda x: x[1], reverse=True)
        
        return scored

# Usage
engine = TFIDFSearchEngine(index)
results = engine.ranked_search("python machine")
for doc_id, score in results:
    print(f"Doc {doc_id}: {score:.3f}")
```

---

## 💡 Complete Example: Production Search System

```python
class ProductionSearchEngine:
    """Complete, optimized search system"""
    
    def __init__(self):
        self.index = PreprocessedInvertedIndex()
        self.tfidf = None
        self.document_cache = {}
    
    def index_documents(self, documents_dict):
        """Index multiple documents"""
        for doc_id, content in documents_dict.items():
            self.index.add_document(content)
        
        # Pre-compute TF-IDF
        self.tfidf = TFIDFSearchEngine(self.index)
    
    def search(self, query, top_k=10):
        """Search and return top K results"""
        results = self.tfidf.ranked_search(query)
        
        return [
            {
                'doc_id': doc_id,
                'score': score,
                'content': self.index.documents[doc_id][:100] + "..."
            }
            for doc_id, score in results[:top_k]
        ]
    
    def get_statistics(self):
        """Report on index"""
        return {
            'total_documents': len(self.index.documents),
            'total_terms': len(self.index.index),
            'avg_terms_per_doc': len(self.index.index) / len(self.index.documents)
        }

# Usage
engine = ProductionSearchEngine()
docs = {
    1: "Python is great for data science",
    2: "Machine learning uses Python",
    3: "Data analysis in Python"
}
engine.index_documents(docs)

results = engine.search("python data", top_k=5)
for result in results:
    print(f"Doc {result['doc_id']}: {result['score']:.3f}")
    print(f"  {result['content']}\n")
```

---

## 🔗 Navigation

**[← Back to Chapter 2](../README.md)** | **[Day 4 Exercises →](./Day-4-Exercises.md)**
