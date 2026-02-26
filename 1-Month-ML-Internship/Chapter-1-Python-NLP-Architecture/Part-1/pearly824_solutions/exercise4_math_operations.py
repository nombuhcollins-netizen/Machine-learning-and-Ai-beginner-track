# Exercise 4: Math Module Operations

import math

# Exercise 4.1: Implement dot product
def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Exercise 4.1 (dot product):", dot_product(v1, v2))


# Exercise 4.2: Implement vector magnitude
def vector_magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

v = [3, 4]

print("Exercise 4.2 (magnitude):", vector_magnitude(v))


# Exercise 4.3: Implement cosine similarity
def cosine_similarity(v1, v2):
    dot = dot_product(v1, v2)
    mag1 = vector_magnitude(v1)
    mag2 = vector_magnitude(v2)
    return dot / (mag1 * mag2)

print("Exercise 4.3 (cosine sim):", round(cosine_similarity(v1, v2), 4))


# Exercise 4.4: Normalize a vector
def normalize(v):
    mag = vector_magnitude(v)
    return [x / mag for x in v]

print("Exercise 4.4 (normalize):", normalize(v))


# Exercise 4.5: Calculate statistics
scores = [78, 85, 92, 88, 76, 95, 89]

mean = sum(scores) / len(scores)

sorted_scores = sorted(scores)
median = sorted_scores[len(scores) // 2]

variance = sum((x - mean) ** 2 for x in scores) / len(scores)
std_dev = math.sqrt(variance)

print("Exercise 4.5:")
print("mean =", round(mean, 2))
print("median =", median)
print("variance =", round(variance, 2))
print("std_dev =", round(std_dev, 2))