# Day 4: Information Retrieval - Exercises

**Difficulty:** Intermediate | **Time:** 6-7 hours | **Capstone:** Inverted Index Builder

---

## 📝 Exercise Set 1: Term-Incidence Matrices

### Exercise 1.1: Build Matrix from Scratch
Create a function that:
- Takes list of documents (strings)
- Builds term-incidence matrix (NumPy array)
- Returns matrix and term list
- Visualizes as heatmap

**File:** `term_incidence_matrix.py`

---

### Exercise 1.2: Matrix Operations
Create class that:
- Builds matrix for document collection
- Calculates matrix statistics
- Finds common terms across documents
- Visualizes patterns

**File:** `matrix_operations.py`

---

### Exercise 1.3: Query with Terms
Implement term-based queries:
- AND: find docs with ALL terms
- OR: find docs with ANY term
- NOT: find docs without term

**File:** `term_queries.py`

---

## 📝 Exercise Set 2: Inverted Index

### Exercise 2.1: Basic Inverted Index
Create `InvertedIndex` class:
- `add_document(content)` - add and index
- `search(word)` - find docs containing word
- `get_document(doc_id)` - retrieve document

**File:** `basic_inverted_index.py`

---

### Exercise 2.2: Inverted Index with Preprocessing
Extend index to include:
- Stop word removal
- Lowercasing
- Punctuation removal
- Stem/lemmatization (optional)

**File:** `preprocessing_inverted_index.py`

---

### Exercise 2.3: Inverted Index Persistence
Implement saving/loading:
- Save index to JSON
- Load index from JSON
- Report index statistics (size, terms, docs)

**File:** `persistent_inverted_index.py`

---

## 📝 Exercise Set 3: Boolean Search

### Exercise 3.1: AND Query
Implement AND query:
- Find docs with ALL search terms
- Return document IDs
- Return full documents

**File:** `boolean_and_query.py`

```python
class BooleanSearchEngine:
    def and_query(self, *terms):
        """Find docs with ALL terms"""
        pass
```

---

### Exercise 3.2: OR Query
Implement OR query:
- Find docs with ANY search term
- Rank by number of matching terms
- Return sorted by relevance

**File:** `boolean_or_query.py`

---

### Exercise 3.3: NOT Query & Combinations
Implement:
- NOT queries
- Combined queries: (A AND B) OR (NOT C)
- Parse query expressions

**File:** `boolean_complex_queries.py`

---

## 📝 Exercise Set 4: Search Optimization

### Exercise 4.1: Index Performance Analysis
Measure performance:
- Time to add documents
- Time to search (O(1)? verify)
- Memory usage
- Compare to linear search

**File:** `index_performance.py`

```python
import time

# Benchmark
start = time.time()
for word in queries:
    results = index.search(word)
elapsed = time.time() - start

print(f"1000 searches in {elapsed:.4f} seconds")
```

---

### Exercise 4.2: Compression Techniques
Implement:
- Set-based index (instead of list)
- Bit-vector compression (optional)
- Memory-efficient storage

**File:** `compressed_index.py`

---

### Exercise 4.3: Parallel Search (Optional)
Implement multi-threaded search:
- Search multiple terms in parallel
- Combine results efficiently
- Measure speedup

**File:** `parallel_search.py`

---

## 📝 Exercise Set 5: Ranking and Relevance

### Exercise 5.1: TF-IDF Scoring
Implement TF-IDF:
- Calculate TF (term frequency in doc)
- Calculate IDF (rarity of term)
- Score documents by TF-IDF

**File:** `tfidf_scoring.py`

```python
class TFIDFRanker:
    def tf(self, term, doc_id):
        # term count / doc length
        pass
    
    def idf(self, term):
        # log(total_docs / docs_with_term)
        pass
    
    def tfidf_score(self, term, doc_id):
        return self.tf(term, doc_id) * self.idf(term)
```

---

### Exercise 5.2: Ranked Search Results
Implement ranked search:
- Search returns sorted results
- Top results most relevant
- Include scores

**File:** `ranked_search.py`

---

### Exercise 5.3: Custom Ranking Algorithms
Implement alternatives to TF-IDF:
- BM25 scoring (optional, advanced)
- Custom relevance function
- A/B test ranking methods

**File:** `custom_ranking.py`

---

## 🎯 Capstone: Inverted Index Builder

### Project: Complete Search System for Document Collection

**Scenario:**
Build a production search system for a document collection with:
- Index building
- Boolean queries
- Ranking
- Performance optimization

**Deliverables:**

#### Part 1: Index Builder (`part1_index_builder.py`)
```python
class DocumentIndexer:
    def __init__(self):
        self.index = InvertedIndex()
        self.tfidf = None
    
    def build_index(self, documents):
        """Load and index documents"""
        for doc_id, content in documents.items():
            self.index.add_document(content)
    
    def get_statistics(self):
        """Report on index"""
        return {
            'documents': len(self.index.documents),
            'terms': len(self.index.index),
            'avg_doc_length': ...
        }
```

#### Part 2: Search Engine (`part2_search_engine.py`)
```python
class SearchEngine:
    def __init__(self, indexer):
        self.indexer = indexer
    
    def search(self, query, method='ranked'):
        """Search with specified method"""
        if method == 'boolean':
            return self.boolean_search(query)
        elif method == 'ranked':
            return self.ranked_search(query)
    
    def boolean_search(self, query):
        # Parse and execute boolean query
        pass
    
    def ranked_search(self, query):
        # TF-IDF ranking
        pass
```

#### Part 3: Query Processor (`part3_query_processor.py`)
```python
class QueryProcessor:
    def parse_query(self, query_string):
        """Parse complex queries"""
        # Handle: (term1 AND term2) OR (NOT term3)
        pass
    
    def execute(self, parsed_query):
        # Execute parsed structure
        pass
```

#### Part 4: Performance Benchmark (`part4_benchmark.py`)
```python
def benchmark_search_engine():
    """Measure performance"""
    
    # Time to build index
    # Time for various queries
    # Memory usage
    # Comparison: indexed vs linear search
    
    report = {
        'index_build_time': ...,
        'avg_query_time': ...,
        'memory_usage': ...,
        'speedup_vs_linear': ...
    }
    return report
```

#### Part 5: Integration & Testing (`part5_integration.py`)
```python
if __name__ == '__main__':
    # Create system
    indexer = DocumentIndexer()
    engine = SearchEngine(indexer)
    
    # Load documents
    docs = load_documents('data/documents/')
    indexer.build_index(docs)
    
    # Show statistics
    print(indexer.get_statistics())
    
    # Test queries
    results = engine.search("python machine learning", method='ranked')
    for doc_id, score in results[:10]:
        print(f"Doc {doc_id}: {score:.3f}")
    
    # Benchmark
    stats = benchmark_search_engine()
    print(f"Average query time: {stats['avg_query_time']:.4f}s")
```

**Success Criteria:**
- [ ] Index built successfully
- [ ] Boolean queries work correctly
- [ ] TF-IDF ranking implemented
- [ ] Performance is fast (O(1) lookup)
- [ ] System handles real datasets
- [ ] Can serialize/deserialize index
- [ ] Comprehensive benchmarking

---

## 📊 Sample Document Collection

For testing, create sample documents:
```python
documents = {
    1: "Python is a programming language",
    2: "Machine learning with Python",
    3: "Data science and analysis",
    4: "Web development using Python",
    5: "Artificial intelligence and ML"
}
```

Or use real data:
- Wikipedia articles (download corpus)
- News articles
- Research papers

---

## 🔗 Navigation

**[← Back to Day 4 Module](./Day-4-Information-Retrieval.md)** | **[Chapter 2 →](../README.md)**
