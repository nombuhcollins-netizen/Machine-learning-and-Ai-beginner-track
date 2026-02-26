# Exercise 1: Master List Comprehensions

# Exercise 1.1: Create a list of squares for numbers 1–20
squares = [x**2 for x in range(1, 21)]
print("Exercise 1.1 result:", squares)

# Exercise 1.2: Filter even numbers from 0–50
evens = [x for x in range(0, 51) if x % 2 == 0]
print("Exercise 1.2 result:", evens)

# Exercise 1.3: Convert list of words to uppercase
words = ["python", "data", "science", "machine", "learning"]
uppercase_words = [word.upper() for word in words]
print("Exercise 1.3 result:", uppercase_words)

# Exercise 1.4: Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested for num in sublist]
print("Exercise 1.4 result:", flattened)

# Exercise 1.5: Create pairs of (number, square, cube)
pairs = [(x, x**2, x**3) for x in range(1, 11)]
print("Exercise 1.5 result:", pairs)