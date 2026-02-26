# Exercise 2: Dictionary Operations for Text

# Exercise 2.1: Count word frequencies in a sentence
text = "the quick brown fox jumps over the lazy dog the fox is quick"

words = text.split()

freq = {word: words.count(word) for word in set(words)}
print("Exercise 2.1:", freq)


# Exercise 2.2: Create word-to-index mapping
word_to_index = {word: idx for idx, word in enumerate(freq.keys())}
index_to_word = {idx: word for word, idx in word_to_index.items()}

print("Exercise 2.2:")
print("word_to_index:", word_to_index)
print("index_to_word:", index_to_word)


# Exercise 2.3: Sort frequencies by count (descending)
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
print("Exercise 2.3:", sorted_freq)


# Exercise 2.4: Top N words
def top_n_words(freq_dict, n=3):
    return sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:n]

print("Exercise 2.4 (top 3):", top_n_words(freq, 3))


# Exercise 2.5: Merge multiple word frequency dictionaries
freq_dict1 = {'apple': 3, 'banana': 2}
freq_dict2 = {'apple': 1, 'cherry': 4}
freq_dict3 = {'banana': 1, 'date': 2}

merged = {}

for d in (freq_dict1, freq_dict2, freq_dict3):
    for key, value in d.items():
        merged[key] = merged.get(key, 0) + value

print("Exercise 2.5:", merged)