# Exercise 5: Edge Case Handling

import math


# Exercise 5.1: Clean mixed whitespace
text_with_whitespace = "Hello   \n\n  World  \r\n  Python  \t\t!"

def clean_whitespace(text):
    return " ".join(text.split())

print("Exercise 5.1:", clean_whitespace(text_with_whitespace))


# Exercise 5.2: Handle unicode characters
text_unicode = "café schöne naïve résumé"

def remove_accents(text):
    return text.encode("ascii", "ignore").decode()

print("Exercise 5.2:", remove_accents(text_unicode))


# Exercise 5.3: Safe file reading with encoding fallback
def read_text_safe(filepath, encoding='utf-8'):
    encodings_to_try = ['utf-8', 'latin-1', 'cp1252']
    
    for enc in encodings_to_try:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    
    raise ValueError("File could not be decoded with supported encodings.")


# Exercise 5.4: Handle division by zero (safe cosine similarity)
def vector_magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

def safe_cosine_similarity(v1, v2):
    mag1 = vector_magnitude(v1)
    mag2 = vector_magnitude(v2)
    
    if mag1 == 0 or mag2 == 0:
        return 0
    
    dot = sum(x * y for x, y in zip(v1, v2))
    return dot / (mag1 * mag2)

print("Exercise 5.4:", safe_cosine_similarity([0, 0], [1, 2]))


# Exercise 5.5: Handle empty/None inputs
texts = ["hello", "", None, "world", ""]

def filter_valid(text_list):
    return [t for t in text_list if isinstance(t, str) and t.strip()]

print("Exercise 5.5:", filter_valid(texts))