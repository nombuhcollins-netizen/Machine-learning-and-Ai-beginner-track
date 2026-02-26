# 02-Loops-Exercises.py

# Exercise 1: Sum Calculator
# Calculate sum of numbers 1 to 100
# Use a for loop
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# Exercise 2: List Processing
# Given a list of scores, print each with a pass/fail indicator
scores = [45, 78, 92, 65, 88, 52, 95]
# Print "PASS" if >= 70, else "FAIL"
for mark in scores:
    if mark >= 70:
        print('PASS')
    else:
        print('FAIL')

# Exercise 3: Pattern Generation
# Create a 5x5 multiplication table using nested loops
for i in range(1,6):
    print()
    for j in range(1,6):
        print(f'{i} * {j} = {i*j}')
# Exercise 4: Word Counter
# Count occurrences of each word
text = "the quick brown fox jumps over the lazy dog the"
words = text.split()
# Create a dictionary with word counts
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

# Exercise 5: ML Data Normalization
raw_data = [100, 50, 75, 25, 90, 60]
# Normalize to 0-1 range using loop
min_val = min(raw_data)
max_val = max(raw_data)
range_val = max_val - min_val
normalize = []
# normalized_data = ...
for num in raw_data:
    normalize.append((num - min_val)/range_val)
print(normalize)