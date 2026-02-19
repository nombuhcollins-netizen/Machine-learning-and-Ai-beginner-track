# Day 5: Exercises - NLP Pipeline Integration (Capstone)

**Date:** Week 1, Day 5 | **Estimated Time:** 4-5 hours | **Difficulty:** Intermediate

---

## Capstone Exercise: Tiny NLP Engine

Create `exercise_tiny_nlp_engine.py` - The complete CLI tool:

```python
#!/usr/bin/env python3
"""
Tiny NLP Engine - Complete text analysis tool
Combines all Week 1 concepts into production-ready system
"""

import argparse
import json
import os
import glob
import re
from pathlib import Path

# Import all components from Week 1 exercises
from exercise1_list_comprehensions import *
from exercise2_dict_operations import *
from exercise3_lambda_functions import *
from exercise4_math_operations import *
from exercise5_edge_cases import *
from exercise6_word_frequency_engine import WordFrequencyEngine
from exercise2_text_cleaning import TextCleaner
from exercise4_stopword_manager import StopwordManager
from exercise6_simple_tokenizer import SimpleTokenizer
from exercise5_document_id_mapper_capstone import DocumentToIDMapper
from exercise5_mini_embedding_engine import MiniEmbeddingEngine

class TinyNLPEngine:
    """
    Complete NLP Engine combining:
    - Text cleaning and preprocessing
    - Tokenization with stopword removal
    - Vocabulary building from corpus
    - Embedding generation
    - Similarity computation
    - CLI interface
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        self.tokenizer = SimpleTokenizer(
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords=True
        )
        self.vocabulary = {}
        self.documents = {}
        self.embeddings = None
    
    # TODO: Implement:
    # - process_directory(path) -> index all files
    # - build_vocabulary() -> create word:index mapping
    # - build_embeddings() -> create similarity space
    # - search_similar(word, k=5) -> find k similar words
    # - export_results(output_dir) -> save all data
    # - get_statistics() -> return corpus stats
    # - interactive_shell() -> REPL for queries
    
    def process_directory(self, directory, pattern='*.txt'):
        """Process all text files in directory"""
        # TODO: Find all matching files
        # TODO: Read and tokenize each
        # TODO: Build vocabulary
        pass
    
    def build_embeddings(self):
        """Create embeddings from processed documents"""
        # TODO: build co-occurrence matrix
        # TODO: normalize vectors
        pass
    
    def search_similar(self, word, k=5):
        """Find k most similar words"""
        # TODO: compute cosine similarities
        # TODO: sort and return top k
        pass
    
    def interactive(self):
        """Interactive query shell"""
        print("Tiny NLP Engine - Interactive Mode")
        print("Commands: query <word>, stats, top <n>, exit")
        print("=" * 50)
        
        while True:
            cmd = input("\n> ").strip()
            
            if not cmd:
                continue
            
            parts = cmd.split()
            command = parts[0].lower()
            
            # TODO: Handle commands
            # - query <word> -> find similar
            # - stats -> show statistics
            # - top <n> -> top N words
            # - exit -> quit
    
    def export_results(self, output_dir):
        """Export vocabulary, embeddings, statistics"""
        # TODO: Save vocabulary as JSON
        # TODO: Save embedding vectors
        # TODO: Save statistics report
        pass
    
    def get_statistics(self):
        """Return corpus statistics"""
        # TODO: Return dict with:
        # - document_count
        # - vocabulary_size
        # - token_count
        # - top_words
        pass

def create_argument_parser():
    """Build CLI argument parser"""
    parser = argparse.ArgumentParser(
        description='Tiny NLP Engine - Text Analysis Tool',
        epilog='Example: python engine.py process --input ./data --output ./results'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Process command
    process_cmd = subparsers.add_parser('process', help='Process text corpus')
    process_cmd.add_argument('--input', required=True, help='Input directory with text files')
    process_cmd.add_argument('--output', required=True, help='Output directory for results')
    process_cmd.add_argument('--pattern', default='*.txt', help='File pattern to match')
    
    # Query command
    query_cmd = subparsers.add_parser('query', help='Find similar words (interactive)')
    query_cmd.add_argument('--vocab', required=True, help='Vocabulary JSON file')
    query_cmd.add_argument('--vectors', required=True, help='Embeddings JSON file')
    
    # Batch query
    batch_cmd = subparsers.add_parser('batch-query', help='Query multiple words')
    batch_cmd.add_argument('--words', required=True, nargs='+', help='Words to query')
    batch_cmd.add_argument('--k', type=int, default=5, help='Number of results per word')
    batch_cmd.add_argument('--vocab', required=True, help='Vocabulary file')
    batch_cmd.add_argument('--vectors', required=True, help='Embeddings file')
    
    # Stats command
    stats_cmd = subparsers.add_parser('stats', help='Show corpus statistics')
    stats_cmd.add_argument('--vocab', required=True, help='Vocabulary file')
    
    return parser

def main():
    """Main entry point"""
    parser = create_argument_parser()
    args = parser.parse_args()
    
    if args.command == 'process':
        # TODO: Process corpus
        engine = TinyNLPEngine()
        engine.process_directory(args.input, args.pattern)
        engine.build_embeddings()
        engine.export_results(args.output)
        print(f"Processing complete. Results saved to {args.output}")
    
    elif args.command == 'query':
        # TODO: Interactive query
        engine = TinyNLPEngine()
        engine.load_from_vocab(args.vocab)
        engine.load_from_vectors(args.vectors)
        engine.interactive()
    
    elif args.command == 'batch-query':
        # TODO: Batch query
        engine = TinyNLPEngine()
        engine.load_from_vocab(args.vocab)
        engine.load_from_vectors(args.vectors)
        
        for word in args.words:
            results = engine.search_similar(word, args.k)
            print(f"\nSimilar to '{word}':")
            for similar_word, score in results:
                print(f"  {similar_word}: {score:.4f}")
    
    elif args.command == 'stats':
        # TODO: Show statistics
        engine = TinyNLPEngine()
        engine.load_from_vocab(args.vocab)
        stats = engine.get_statistics()
        print(json.dumps(stats, indent=2))
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
```

---

## Implementation Checklist

Week 1 Capstone Requirements:

✅ Tokenizer with all cleaning options
✅ Vocabulary builder from multiple documents
✅ Embedding engine with co-occurrence matrices
✅ Similarity computation (cosine)
✅ CLI interface with multiple commands
✅ Export/Import functionality
✅ Statistics and reporting
✅ Interactive query shell
✅ Error handling for edge cases
✅ Full Git commit history

---

## Testing Checklist

Before completing Week 1:

```bash
# Process corpus
python exercise_tiny_nlp_engine.py process --input ./sample_texts --output ./results

# View statistics
python exercise_tiny_nlp_engine.py stats --vocab ./results/vocabulary.json

# Interactive queries
python exercise_tiny_nlp_engine.py query --vocab ./results/vocabulary.json --vectors ./results/vectors.json

# Batch query
python exercise_tiny_nlp_engine.py batch-query --words machine learning deep --vocab ./results/vocabulary.json --vectors ./results/vectors.json
```

---

## Final Commit

```bash
git add exercise_tiny_nlp_engine.py
git commit -m "feat: Complete Day 5 Capstone - Tiny NLP Engine (Full CLI Tool)"

git add *.py  # All Week 1 exercises
git commit -m "docs: Complete Week 1 - Python & NLP Architecture all exercises and capstone"
```

---

## Week 1 Recap

You've learned and implemented:

✅ Advanced Python data structures and functions
✅ Text cleaning and preprocessing with regex
✅ Tokenization and stopword removal
✅ File indexing and vocabulary building
✅ Vector embeddings and similarity computation
✅ Complete NLP pipeline integration
✅ Production-ready CLI tool

**You now understand the complete pipeline of how NLP systems work from first principles!**

---

**[← Back to Chapter 1](./README.md)** | **[Next: Chapter 2 (Week 2) →](../Chapter-2-Data-Intensive-Search/README.md)**
