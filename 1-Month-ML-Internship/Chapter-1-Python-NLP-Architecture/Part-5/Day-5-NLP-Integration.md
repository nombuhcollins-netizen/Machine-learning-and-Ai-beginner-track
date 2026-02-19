# Day 5: NLP Pipeline Integration

**Date:** Week 1, Day 5 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

✅ Combine all Week 1 components into integrated pipeline
✅ Implement modular design patterns
✅ Build CLI interface for text analysis
✅ Create reusable NLP components
✅ Handle real-world text processing workflows
✅ Deploy complete Tiny NLP Engine

---

## 📖 Core Topics

### 1. Modular Architecture

```python
class TinyNLPEngine:
    """
    Complete NLP Engine combining all Week 1 components.
    
    Pipeline:
    Raw Text → Clean → Tokenize → Vocabulary Build → Embed → Similarity
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        self.tokenizer = SimpleTokenizer(
            lowercase=True,
            remove_stopwords=True,
            remove_punctuation=True
        )
        self.vocabulary = DynamicVocabulary()
        self.embedding_engine = None
        self.documents = {}
    
    def process_document(self, text, doc_id=None):
        """Process single document through pipeline"""
        # Clean
        text = self._clean_text(text)
        
        # Tokenize
        tokens = self.tokenizer.process(text)
        
        # Build vocabulary
        self.vocabulary.add_words(tokens)
        
        # Store
        if doc_id:
            self.documents[doc_id] = tokens
        
        return tokens
    
    def build_embeddings(self):
        """Build embedding space from vocabulary"""
        all_tokens = []
        for tokens in self.documents.values():
            all_tokens.extend(tokens)
        
        self.embedding_engine = EmbeddingEngine(self.vocabulary)
        self.embedding_engine.build_cooccurrence(all_tokens)
    
    def find_similar(self, word, k=5):
        """Find similar words"""
        if not self.embedding_engine:
            raise ValueError("Must build embeddings first")
        
        return self.embedding_engine.find_similar(word, k)
    
    def _clean_text(self, text):
        """Clean text: encoding, whitespace, URLs"""
        # Normalize unicode
        import unicodedata
        text = unicodedata.normalize('NFD', text)
        
        # Remove URLs
        import re
        text = re.sub(r'http[s]?://\S+', '', text)
        
        # Normalize whitespace
        text = ' '.join(text.split())
        
        return text
```

### 2. CLI Interface with argparse

```python
import argparse
import json

def create_cli():
    """Build command-line interface"""
    parser = argparse.ArgumentParser(
        description='Tiny NLP Engine - Text Analysis Tool'
    )
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Process command
    process_parser = subparsers.add_parser('process', help='Process text files')
    process_parser.add_argument('--input', required=True, help='Input directory or file')
    process_parser.add_argument('--output', required=True, help='Output directory')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Find similar words')
    query_parser.add_argument('--word', required=True, help='Word to query')
    query_parser.add_argument('--k', type=int, default=5, help='Number of results')
    query_parser.add_argument('--vocab', required=True, help='Vocabulary file')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    stats_parser.add_argument('--vocab', required=True, help='Vocabulary file')
    
    return parser

def main():
    """Main CLI entry point"""
    parser = create_cli()
    args = parser.parse_args()
    
    if args.command == 'process':
        engine = TinyNLPEngine()
        # Process files from args.input
        # Save vocabulary to args.output
        pass
    
    elif args.command == 'query':
        # Load vocabulary
        # Find similar words
        # Display results
        pass
    
    elif args.command == 'stats':
        # Load vocabulary
        # Display statistics
        pass

if __name__ == '__main__':
    main()
```

### 3. Complete Integration

```python
class TinyNLPEngineFull:
    """Full-featured NLP engine with all components"""
    
    def __init__(self):
        self.tokenizer = SimpleTokenizer()
        self.doc_indexer = DocumentIndexer()
        self.embedding_engine = None
        
    def process_corpus(self, corpus_dir):
        """Load and process entire corpus"""
        print(f"Processing corpus from {corpus_dir}...")
        
        self.doc_indexer.index_directory(
            corpus_dir,
            self.tokenizer,
            pattern='*.txt'
        )
        
        print(f"Indexed {len(self.doc_indexer.documents)} documents")
        print(f"Vocabulary size: {self.doc_indexer.vocabulary.size()}")
        
        # Build embeddings
        all_tokens = []
        for tokens in self.doc_indexer.documents.values():
            all_tokens.extend(tokens)
        
        self.embedding_engine = EmbeddingEngine(self.doc_indexer.vocabulary)
        self.embedding_engine.build_cooccurrence(all_tokens)
        
        return self._get_stats()
    
    def _get_stats(self):
        """Get corpus statistics"""
        return {
            'documents': len(self.doc_indexer.documents),
            'vocabulary_size': self.doc_indexer.vocabulary.size(),
            'top_words': self.doc_indexer.vocabulary.get_top_words(20)
        }
    
    def search(self, word, k=5):
        """Search for similar words"""
        if not self.embedding_engine:
            raise ValueError("Must process corpus first")
        
        results = self.embedding_engine.find_similar(word, k)
        return results
    
    def export(self, output_dir):
        """Export all data"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Export vocabulary
        self.doc_indexer.export_vocabulary(
            os.path.join(output_dir, 'vocabulary.json')
        )
        
        print(f"Exported to {output_dir}")
```

---

**[← Back to Chapter 1](./README.md)** | **[Day 5 Exercises →](./Day-5-Exercises.md)**
