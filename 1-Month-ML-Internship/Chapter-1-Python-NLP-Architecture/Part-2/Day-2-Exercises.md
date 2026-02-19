# Day 2: Exercises - Text Cleaning & NLP Preprocessing

**Date:** Week 1, Day 2 | **Estimated Time:** 3-4 hours | **Difficulty:** Foundational

---

## Exercise Set 1: Regular Expressions for Text Cleaning

### Exercise 1.1: Email and URL Extraction
Create `exercise1_regex_patterns.py`:

```python
import re

# Exercise 1.1a: Extract all email addresses from text
emails_text = """
Contact us at support@example.com or sales@mycompany.net.
For inquiries: john.doe@service.co.uk
"""
# TODO: Extract all valid emails using regex

# Exercise 1.1b: Remove URLs from text
text_with_urls = """
Visit our website at https://www.example.com for more info.
Check https://blog.example.org/article-123 for updates.
FTP: ftp://files.example.com/data/
"""
# TODO: Remove all URLs using re.sub()

# Exercise 1.1c: Extract hashtags and mentions
social_text = """
@john_doe just shared #python #NLP #machinelearning content
@jane_smith commented on #AI #technology #future
"""
# TODO: Extract all @mentions
# TODO: Extract all #hashtags

# Exercise 1.1d: Normalize whitespace
messy_text = "Hello    \n\n   World  \t\t  Python  \r\n  !"
# TODO: Normalize to single spaces

# Exercise 1.1e: Extract numbers and measurements
text = "The laptop costs $999.99. Temperature is 75.5 degrees. ID: 123456"
# TODO: Extract all numbers (including decimals)
```

**Expected Outputs:**
```
1.1a: ['support@example.com', 'sales@mycompany.net', 'john.doe@service.co.uk']
1.1b: 'Visit our website at  for more info.\nCheck  for updates.\nFTP: '
1.1c mentions: ['@john_doe', '@jane_smith']
1.1c hashtags: ['#python', '#NLP', '#machinelearning', '#AI', '#technology', '#future']
1.1d: "Hello World Python !"
1.1e: ['999.99', '75.5', '123456']
```

---

### Exercise 1.2: Text Cleaning Pipeline
Create `exercise2_text_cleaning.py`:

```python
import re

class TextCleaner:
    """Multi-purpose text cleaning utility"""
    
    def __init__(self):
        self.url_pattern = r'http[s]?://\S+'
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # TODO: Implement methods:
    # - remove_urls(text) -> text without URLs
    # - remove_emails(text) -> text without emails
    # - remove_special_chars(text, keep=None) -> only alphanumeric
    # - normalize_whitespace(text) -> single spaces
    # - expand_contractions(text) -> don't -> do not
    # - to_lowercase(text)
    # - to_uppercase(text)

# Test the cleaner
cleaner = TextCleaner()
text = """
Visit https://example.com for info. 
Email: help@example.com
I don't think he won't come!
Temperature: 75.5°C  ...
"""
# TODO: Apply full cleaning pipeline
```

---

## Exercise Set 2: Stopword Management

### Exercise 2.1: Stopword Filtering
Create `exercise3_stopwords.py`:

```python
# Default stopwords
STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the',
    'to', 'was', 'will', 'with', 'i', 'me', 'my', 'you', 'him', 'her',
    'this', 'but', 'not', 'which', 'who', 'when', 'where', 'why'
}

# Exercise 2.1a: Remove stopwords from text
text = "The quick brown fox jumps over the lazy dog in the morning"
words = text.split()
# TODO: Filter stopwords, keep only important words

# Exercise 2.1b: Create custom stopword set
custom_stopwords = STOPWORDS.copy()
custom_stopwords.add('fox')
custom_stopwords.add('dog')
# TODO: Filter with custom stopwords

# Exercise 2.1c: Stopword statistics
long_text = """
The machine learning model is important. The model learns from data.
The algorithm processes the features. Features are the data.
"""
words = long_text.lower().split()
# TODO: Count stopwords vs. content words
# Output: {'stopwords': count, 'content_words': count, 'ratio': percentage}
```

### Exercise 2.2: StopwordManager Class
Create `exercise4_stopword_manager.py`:

```python
class StopwordManager:
    """Advanced stopword management"""
    
    def __init__(self, language='english'):
        self.language = language
        self.stopwords = self._load_stopwords()
        self.custom_additions = set()
        self.custom_removals = set()
    
    # TODO: Implement:
    # - add_stopword(word) -> add to custom list
    # - remove_stopword(word) -> remove from main list
    # - get_all_stopwords() -> combined set
    # - is_stopword(word) -> boolean
    # - filter_tokens(word_list) -> filtered words
    # - save_custom(filepath) -> export custom stopwords
    # - load_custom(filepath) -> import custom stopwords

# Test usage
manager = StopwordManager()
manager.add_stopword('python')  # Domain-specific
manager.add_stopword('learning')

text = "Python machine learning is powerful python framework learning tool"
words = text.lower().split()
filtered = manager.filter_tokens(words)
# Output: ['machine', 'powerful', 'framework', 'tool']
```

---

## Exercise Set 3: N-gram Generation

### Exercise 3.1: N-gram Operations
Create `exercise5_ngrams.py`:

```python
# Exercise 3.1a: Generate unigrams, bigrams, trigrams
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# TODO: Generate unigrams (single words)
# TODO: Generate bigrams (word pairs)
# TODO: Generate trigrams (word triplets)

# Exercise 3.1b: Count n-gram frequencies
# Use the same text
# TODO: Count bigram frequencies
# TODO: Return top 5 most frequent bigrams

# Exercise 3.1c: Character-level n-grams
word = "python"
# TODO: Generate character bigrams (e.g., 'py', 'yt', 'th', 'ho', 'on')
# TODO: Generate character trigrams

# Exercise 3.1d: Skip-grams (n-grams with gaps)
words = ['the', 'quick', 'brown', 'fox', 'jumps']
# TODO: Generate bigrams skipping every other word
# Output: [('the', 'brown'), ('quick', 'fox'), ('brown', 'jumps')]

# Exercise 3.1e: N-gram statistics
long_text = "the dog and the cat and the mouse and the bird"
words = long_text.split()
# TODO: Count unigrams, bigrams, trigrams
# Output: {'unigrams': 9, 'bigrams': 8, 'trigrams': 7}
```

**Expected Outputs:**
```
3.1a unigrams: [('the',), ('quick',), ('brown',), ...]
3.1a bigrams: [('the', 'quick'), ('quick', 'brown'), ('brown', 'fox'), ...]
3.1b top 5: [('the', 'and'), ('and', 'the'), ('dog', 'and'), ('cat', 'and'), ('mouse', 'and')]
3.1c char bigrams: ['py', 'yt', 'th', 'ho', 'on']
3.1d skip-bigrams: [('the', 'brown'), ('quick', 'fox'), ('brown', 'jumps')]
```

---

## Exercise Set 4: SimpleTokenizer Class

### Exercise 4.1: Complete Tokenizer Implementation
Create `exercise6_simple_tokenizer.py`:

```python
import re

class SimpleTokenizer:
    """
    Complete tokenizer from scratch implementing all Day 2 concepts.
    """
    
    def __init__(self, lowercase=True, remove_punctuation=True, 
                 remove_stopwords=False, min_length=1):
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords
        self.min_length = min_length
        self.stopwords = self._get_stopwords()
    
    @staticmethod
    def _get_stopwords():
        return {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the',
            'to', 'was', 'will', 'with', 'this', 'but', 'not'
        }
    
    # TODO: Implement .clean(text) -> str
    # TODO: Implement .tokenize(text) -> list
    # TODO: Implement .remove_stopwords(tokens) -> list
    # TODO: Implement .process(text) -> list (complete pipeline)
    # TODO: Implement .generate_ngrams(tokens, n) -> list
    
    def get_statistics(self, tokens):
        """Calculate statistics for tokens"""
        # TODO: Return {'count': int, 'unique': int, 'avg_length': float}
        pass

# Test cases
tokenizer = SimpleTokenizer(lowercase=True, remove_stopwords=True)

test_text1 = "The QUICK brown fox JUMPS over the lazy dog!!!"
result1 = tokenizer.process(test_text1)
# Expected: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']

test_text2 = "Python is GREAT! Python is FUN! python.is.powerful"
result2 = tokenizer.process(test_text2)
# Expected: ['python', 'great', 'python', 'fun', 'python', 'powerful']

# Test n-gram generation
bigrams = tokenizer.generate_ngrams(result1, 2)
# Expected: [('quick', 'brown'), ('brown', 'fox'), ...]

# Test statistics
stats = tokenizer.get_statistics(result1)
# Expected: {'count': 6, 'unique': 6, 'avg_length': ~4.3}
```

---

## Exercise Set 5: Unicode Handling

### Exercise 5.1: Unicode Normalization
Create `exercise7_unicode_handling.py`:

```python
import unicodedata

# Exercise 5.1a: Remove accents
# TODO: Function remove_accents(text) using unicodedata.normalize()
texts = [
    "café schöne naïve résumé",
    "Zürich Montréal pêche",
    "Москва москва"  # Cyrillic won't change
]
# TODO: Apply removing accents

# Exercise 5.1b: Normalize different unicode forms
# TODO: NFD (decomposed) vs NFC (composed)
text = "é"  # Single character (NFC)
nfd = unicodedata.normalize('NFD', text)  # Two characters (N + accent)
# Demonstrate difference

# Exercise 5.1c: Remove non-ASCII characters
# TODO: Function strip_non_ascii(text)
text_with_emoji = "Hello 👋 World 🌍! Python 🐍 rocks!"
# TODO: Remove emoji and non-ASCII

# Exercise 5.1d: Encoding/Decoding
# TODO: Handle bytes with different encodings
data = "café".encode('utf-8')  # bytes
# TODO: Decode safely with fallback encodings
```

---

## Exercise Set 6: Capstone - SimpleTokenizer Capstone

### Exercise 6: Complete NLP Pipeline
Create `exercise8_nlp_pipeline_capstone.py`:

```python
import re
from collections import defaultdict

class NLPPipeline:
    """
    Complete NLP preprocessing pipeline combining all Day 2 concepts.
    """
    
    def __init__(self):
        self.tokenizer = SimpleTokenizer(
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords=True,
            min_length=2
        )
        self.documents = {}
        self.vocabulary = {}
    
    # TODO: Implement:
    # - process_text(text) -> dict with full analysis
    # - process_file(filepath) -> load and process
    # - process_multiple_files(file_list) -> batch process
    # - get_vocabulary() -> unique words across all docs
    # - export_stats(filepath) -> save statistics
    # - export_tokens(filepath) -> save all tokens
    
    def process_text(self, text, doc_id=None):
        """Complete processing: clean → tokenize → analyze"""
        # TODO: Return {
        #   'tokens': [...],
        #   'token_count': int,
        #   'unique_count': int,
        #   'bigrams': [...top 10],
        #   'trigrams': [...top 5],
        #   'statistics': {...}
        # }
        pass

# Test the pipeline
pipeline = NLPPipeline()

doc1 = """
Machine learning is a branch of artificial intelligence.
Machine learning focuses on learning from data.
Deep learning is a subset of machine learning.
"""

doc2 = """
Natural language processing concerns human language.
NLP uses machine learning techniques.
Text classification is an NLP task.
"""

result1 = pipeline.process_text(doc1, 'doc1')
result2 = pipeline.process_text(doc2, 'doc2')

print(f"Doc1 tokens: {len(result1['tokens'])}")
print(f"Doc1 unique: {result1['unique_count']}")
print(f"Doc1 top bigrams: {result1['bigrams'][:5]}")

print(f"\nDoc2 tokens: {len(result2['tokens'])}")
print(f"Doc2 unique: {result2['unique_count']}")
print(f"Doc2 top bigrams: {result2['bigrams'][:5]}")
```

---

## Commit Strategy

```bash
git add exercise1_regex_patterns.py
git commit -m "feat: Complete Day 2 Exercise 1 - Regex Patterns"

git add exercise2_text_cleaning.py
git commit -m "feat: Complete Day 2 Exercise 2 - Text Cleaning Pipeline"

git add exercise3_stopwords.py
git commit -m "feat: Complete Day 2 Exercise 3 - Stopword Filtering"

git add exercise4_stopword_manager.py
git commit -m "feat: Complete Day 2 Exercise 4 - Stopword Manager Class"

git add exercise5_ngrams.py
git commit -m "feat: Complete Day 2 Exercise 5 - N-gram Generation"

git add exercise6_simple_tokenizer.py
git commit -m "feat: Complete Day 2 Exercise 6 - SimpleTokenizer Class"

git add exercise7_unicode_handling.py
git commit -m "feat: Complete Day 2 Exercise 7 - Unicode Handling"

git add exercise8_nlp_pipeline_capstone.py
git commit -m "feat: Complete Day 2 Exercise 8 - NLP Pipeline Capstone"
```

---

## Self-Assessment

✅ Can write regex patterns for common tasks
✅ Implement stopword filtering
✅ Generate n-grams at word and character level
✅ Build class-based tokenizers
✅ Handle unicode and encoding issues
✅ Process complete text documents
✅ All code committed and working

---

**[← Back to Day 2 Module](./Day-2-Text-Preprocessing.md)** | **[Day 3 Module →](./Day-3-File-Indexing.md)**
