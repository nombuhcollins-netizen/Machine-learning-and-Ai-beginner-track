# Exercise 3: Lambda Functions & Functional Programming

from functools import reduce

# Exercise 3.1: Filter words longer than 3 characters
words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]

long_words = list(filter(lambda word: len(word) > 3, words))
print("Exercise 3.1:", long_words)


# Exercise 3.2: Transform (double) all numbers in a list
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print("Exercise 3.2:", doubled)


# Exercise 3.3: Sort students by grade (descending), then by name
students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 85),
    ('David', 78),
    ('Eve', 92)
]

sorted_students = sorted(students, key=lambda s: (-s[1], s[0]))
print("Exercise 3.3:", sorted_students)


# Exercise 3.4: Filter and transform in one step
# Keep only odd numbers and cube them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_cubes = list(map(lambda x: x**3, filter(lambda x: x % 2 != 0, numbers)))
print("Exercise 3.4:", odd_cubes)


# Exercise 3.5: Sum with condition using reduce
# Sum of squares for even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares_sum = reduce(
    lambda acc, x: acc + x**2,
    filter(lambda x: x % 2 == 0, numbers),
    0
)

print("Exercise 3.5:", even_squares_sum)