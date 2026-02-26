# Exercise 6: Capstone - Word Frequency Engine

import json
import math
from functools import reduce
from collections import defaultdict


class WordFrequencyEngine:
    """
    Advanced word frequency analyzer combining Day 1 concepts.
    """

    def __init__(self, min_word_length=2):
        self.min_word_length = min_word_length
        self.vocabularies = {}  # Stores frequencies per file

    def clean_text(self, text):
        """Normalize whitespace and lowercase text."""
        return " ".join(text.split()).lower()

    def tokenize(self, text):
        """Split text into words and filter by minimum length."""
        return [word for word in text.split() if len(word) >= self.min_word_length]

    def count_frequencies(self, words):
        """Count word frequencies using defaultdict."""
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        return dict(freq)

    def analyze_text(self, text):
        """Full pipeline: clean → tokenize → count."""
        cleaned = self.clean_text(text)
        tokens = self.tokenize(cleaned)
        return self.count_frequencies(tokens)

    def process_multiple_files(self, file_list):
        """Read and analyze multiple text files safely."""
        for filepath in file_list:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='latin-1') as f:
                    text = f.read()

            self.vocabularies[filepath] = self.analyze_text(text)

    def top_n_words(self, n=10):
        """Return top N words across all vocabularies."""
        combined = defaultdict(int)

        for vocab in self.vocabularies.values():
            for word, count in vocab.items():
                combined[word] += count

        return sorted(combined.items(), key=lambda x: x[1], reverse=True)[:n]

    def calculate_statistics(self):
        """Calculate min, max, mean frequency."""
        combined = defaultdict(int)

        for vocab in self.vocabularies.values():
            for word, count in vocab.items():
                combined[word] += count

        if not combined:
            return {"min": 0, "max": 0, "mean": 0}

        values = list(combined.values())

        min_freq = min(values)
        max_freq = max(values)
        mean_freq = reduce(lambda a, b: a + b, values) / len(values)

        return {
            "min": min_freq,
            "max": max_freq,
            "mean": round(mean_freq, 2)
        }

    def get_statistics(self):
        """Public wrapper for statistics."""
        return self.calculate_statistics()

    def save_to_json(self, filepath):
        """Export vocabularies to JSON."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.vocabularies, f, indent=4)


# Example Usage (Safe Demo)
if __name__ == "__main__":
    engine = WordFrequencyEngine(min_word_length=3)

    sample_text = "Python is powerful and Python is fun to learn"
    freqs = engine.analyze_text(sample_text)

    engine.vocabularies["sample"] = freqs

    print("Top words:", engine.top_n_words(5))
    print("Statistics:", engine.get_statistics())

    engine.save_to_json("output.json")