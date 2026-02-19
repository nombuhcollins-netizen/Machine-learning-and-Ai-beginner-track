# Day 2: Text Cleaning & NLP Preprocessing

**Date:** Week 1, Day 2 | **Duration:** 7+ Hours | **Difficulty:** Foundational

---

## 🎯 Learning Objectives

By the end of Day 2, you will:

✅ Master regular expressions (regex) for pattern matching
✅ Implement stopword filtering logic
✅ Generate n-grams (unigrams, bigrams, trigrams)
✅ Design and build a class-based tokenizer
✅ Handle Unicode and text encoding issues
✅ Prepare text data for ML pipelines

---

## 📖 Core Topics

### 1. Regular Expressions (Regex) for Text Cleaning

#### Basic Patterns
```python
import re

# Pattern basics
text = "Hello123 World456! Python@2024"

# Find all words (letters only)
words = re.findall(r'\b[a-zA-Z]+\b', text)
# Output: ['Hello', 'World', 'Python']

# Find all numbers
numbers = re.findall(r'\d+', text)
# Output: ['123', '456', '2024']

# Remove special characters
clean = re.sub(r'[^a-zA-Z0-9\s]', '', text)
# Output: 'Hello123 World456 Python2024'
```

#### Common Text Cleaning Patterns
```python
def clean_email(email):
    """Extract valid email addresses"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, email)

def extract_hashtags(text):
    """Extract hashtags from text"""
    return re.findall(r'#\w+', text)

def extract_mentions(text):
    """Extract @mentions from text"""
    return re.findall(r'@\w+', text)

def normalize_whitespace(text):
    """Replace multiple spaces/tabs with single space"""
    return re.sub(r'\s+', ' ', text).strip()

def remove_urls(text):
    """Remove URLs from text"""
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
```

#### Regex Substitution with Functions
```python
def expand_contractions(text):
    """Expand contractions like don't -> do not"""
    contractions_dict = {
        r"don't": "do not",
        r"can't": "cannot",
        r"won't": "will not",
        r"n't": " not",
        r"'re": " are",
        r"'ve": " have",
    }
    
    for pattern, replacement in contractions_dict.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

# Usage
text = "I don't think he won't come"
expanded = expand_contractions(text)
# Output: "I do not think he will not come"
```

---

### 2. Stopword Filtering Logic

#### Built-in Stopwords
```python
# Common English stopwords
STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the',
    'to', 'was', 'will', 'with', 'i', 'me', 'my', 'you', 'him', 'her'
}

def remove_stopwords(words, stopwords=STOPWORDS):
    """Filter out stopwords from word list"""
    return [w for w in words if w.lower() not in stopwords]

# Usage
sentence = "the quick brown fox jumped over the lazy dog"
words = sentence.split()
filtered = remove_stopwords(words)
# Output: ['quick', 'brown', 'fox', 'jumped', 'lazy', 'dog']
```

#### Custom Stopword Management
```python
class StopwordManager:
    """Manage custom stopwords per language"""
    
    def __init__(self, language='english'):
        self.language = language
        self.stopwords = self._load_stopwords()
        self.custom_stopwords = set()
    
    def _load_stopwords(self):
        """Load default stopwords"""
        # In production, load from file or library
        return STOPWORDS
    
    def add_stopword(self, word):
        """Add custom stopword"""
        self.custom_stopwords.add(word.lower())
    
    def add_stopwords(self, words):
        """Add multiple custom stopwords"""
        self.custom_stopwords.update(w.lower() for w in words)
    
    def get_all_stopwords(self):
        """Get combined stopwords"""
        return self.stopwords | self.custom_stopwords
    
    def is_stopword(self, word):
        """Check if word is stopword"""
        return word.lower() in self.get_all_stopwords()
    
    def filter(self, words):
        """Filter stopwords from word list"""
        return [w for w in words if not self.is_stopword(w)]

# Usage
manager = StopwordManager()
manager.add_stopword('python')  # Domain-specific
filtered = manager.filter(['the', 'quick', 'python', 'fox'])
# Output: ['quick', 'fox']
```

---

### 3. N-gram Generation

#### Unigram, Bigram, Trigram
```python
def generate_ngrams(words, n=2):
    """Generate n-grams from word list"""
    return [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]

# Usage
text = "the quick brown fox"
words = text.split()

unigrams = generate_ngrams(words, 1)
# Output: [('the',), ('quick',), ('brown',), ('fox',)]

bigrams = generate_ngrams(words, 2)
# Output: [('the', 'quick'), ('quick', 'brown'), ('brown', 'fox')]

trigrams = generate_ngrams(words, 3)
# Output: [('the', 'quick', 'brown'), ('quick', 'brown', 'fox')]
```

#### Counting N-grams
```python
def count_ngrams(words, n=2):
    """Count frequency of n-grams"""
    ngrams = generate_ngrams(words, n)
    freq = {}
    for gram in ngrams:
        freq[gram] = freq.get(gram, 0) + 1
    return freq

# Usage
text = "the dog and the cat and the mouse"
words = text.split()

bigram_freq = count_ngrams(words, 2)
# Output: {('the', 'dog'): 1, ('dog', 'and'): 1, ('and', 'the'): 2, ...}

# Top bigrams
top_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)
```

#### Character-level N-grams
```python
def generate_char_ngrams(text, n=3):
    """Generate character-level n-grams"""
    text = text.replace(' ', '_')  # Preserve word boundaries
    return [text[i:i+n] for i in range(len(text) - n + 1)]

# Usage
word = "python"
trigrams = generate_char_ngrams(word, 3)
# Output: ['pyt', 'yth', 'tho', 'hon']
```

---

### 4. Class-Based Tokenizer Design

#### Complete Tokenizer Class
```python
import re

class SimpleTokenizer:
    """
    A class-based tokenizer implementing all Day 2 concepts.
    """
    
    def __init__(self, lowercase=True, remove_punctuation=True, 
                 remove_stopwords=False, min_length=1):
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords
        self.min_length = min_length
        self.stopwords = self._default_stopwords()
    
    @staticmethod
    def _default_stopwords():
        """Get default English stopwords"""
        return {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the',
            'to', 'was', 'will', 'with', 'i', 'me', 'my', 'you', 'him', 'her'
        }
    
    def clean(self, text):
        """
        Clean text: normalize whitespace, encoding, URLs.
        
        Args:
            text (str): Raw text input
        
        Returns:
            str: Cleaned text
        """
        # Remove URLs
        text = re.sub(r'http[s]?://\S+', '', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Lowercase if enabled
        if self.lowercase:
            text = text.lower()
        
        return text.strip()
    
    def tokenize(self, text):
        """
        Tokenize text into words.
        
        Args:
            text (str): Cleaned text (use clean() first)
        
        Returns:
            list: List of tokens (words)
        """
        # Remove punctuation if enabled
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)
        
        # Split into tokens
        tokens = text.split()
        
        # Filter by minimum length
        tokens = [t for t in tokens if len(t) >= self.min_length]
        
        return tokens
    
    def remove_stopwords_fn(self, tokens):
        """
        Remove stopwords from token list.
        
        Args:
            tokens (list): List of tokens
        
        Returns:
            list: Tokens without stopwords
        """
        return [t for t in tokens if t.lower() not in self.stopwords]
    
    def process(self, text):
        """
        Complete processing pipeline: clean → tokenize → remove stopwords.
        
        Args:
            text (str): Raw text input
        
        Returns:
            list: Processed tokens
        """
        text = self.clean(text)
        tokens = self.tokenize(text)
        if self.remove_stopwords:
            tokens = self.remove_stopwords_fn(tokens)
        return tokens
    
    def generate_ngrams(self, tokens, n=2):
        """Generate n-grams from tokens"""
        return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

# Usage Example
tokenizer = SimpleTokenizer(lowercase=True, remove_stopwords=True)
text = "The QUICK brown fox JUMPS over the lazy dog!!!"
tokens = tokenizer.process(text)
print(f"Tokens: {tokens}")
# Output: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']

bigrams = tokenizer.generate_ngrams(tokens, 2)
print(f"Bigrams: {bigrams}")
# Output: [('quick', 'brown'), ('brown', 'fox'), ...]
```

---

### 5. Unicode and Encoding Handling

#### Unicode Normalization
```python
import unicodedata

def normalize_unicode(text):
    """Normalize unicode to decomposed form (NFD)"""
    return unicodedata.normalize('NFD', text)

def remove_accents(text):
    """Remove accents from unicode characters"""
    nfd = unicodedata.normalize('NFD', text)
    return ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')

# Usage
text = "café schöne naïve résumé"
cleaned = remove_accents(text)
# Output: "cafe schone naive resume"
```

#### Encoding Detection and Handling
```python
def safe_decode(data, encodings=['utf-8', 'latin-1', 'cp1252']):
    """Safely decode bytes with fallback encodings"""
    for encoding in encodings:
        try:
            return data.decode(encoding)
        except (UnicodeDecodeError, AttributeError):
            continue
    return data.decode('utf-8', errors='ignore')
```

---

## 💡 Complete Example: Text Preprocessing Pipeline

```python
class TextProcessor:
    """Complete text processing pipeline"""
    
    def __init__(self):
        self.tokenizer = SimpleTokenizer(
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords=True
        )
    
    def process_document(self, text):
        """Process a complete document"""
        tokens = self.tokenizer.process(text)
        
        return {
            'tokens': tokens,
            'token_count': len(tokens),
            'unique_tokens': len(set(tokens)),
            'avg_token_length': sum(len(t) for t in tokens) / len(tokens) if tokens else 0,
            'bigrams': self.tokenizer.generate_ngrams(tokens, 2),
            'trigrams': self.tokenizer.generate_ngrams(tokens, 3)
        }

# Usage
processor = TextProcessor()
text = """
Machine learning is a subset of artificial intelligence.
It focuses on enabling computers to learn from data.
Deep learning uses neural networks with multiple layers.
"""
result = processor.process_document(text)
print(f"Tokens: {result['tokens']}")
print(f"Token count: {result['token_count']}")
print(f"Bigrams: {result['bigrams'][:5]}")  # First 5 bigrams
```

---

## 🔗 Navigation

**[← Back to Chapter 1](./README.md)** | **[Day 2 Exercises →](./Day-2-Exercises.md)**
