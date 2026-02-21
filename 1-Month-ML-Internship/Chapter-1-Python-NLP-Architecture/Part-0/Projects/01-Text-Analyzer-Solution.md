# Project 1 Solution: Text Analyzer

\`\`\`python
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def analyze_text(text):
    words = text.lower().split()
    word_count = len(words)
    char_count = len(text)
    unique_words = len(set(words))
    
    # Word frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
    
    # Sentence count
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    return {
        'words': word_count,
        'chars': char_count,
        'unique': unique_words,
        'frequency': freq,
        'avg_length': avg_word_length,
        'sentences': sentences
    }

def save_report(filename, analysis):
    with open(filename, 'w') as f:
        f.write("TEXT ANALYSIS REPORT")
        f.write("=" * 50)
        for key, value in analysis.items():
            f.write(f"{key}: {value}\n")

# Main
text = read_file("sample.txt")
analysis = analyze_text(text)
save_report("report.txt", analysis)
\`\`\`

---
