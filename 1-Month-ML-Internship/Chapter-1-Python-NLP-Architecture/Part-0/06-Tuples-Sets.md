# 06: Tuples & Sets - Immutable & Unique Collections

**Duration:** 40 minutes | **Difficulty:** Beginner | **Key Skill:** Other data structures

---

## í¾¯ What You'll Learn

- Creating and using tuples (immutable sequences)
- Creating and using sets (unique collections)
- When to use each data structure
- ML Context: Tuples for immutable data, sets for deduplication

---

## í³š Tuples: Immutable Sequences

### Creating Tuples

\`\`\`python
# Tuples are like lists but IMMUTABLE (can't change)
coordinates = (10, 20)
color = ("red", "green", "blue")
single_item = (42,)  # Note the comma!
empty = ()

# Access like lists
print(coordinates[0])  # 10
print(color[-1])       # "blue"
\`\`\`

### Why Use Tuples?

1. **Performance** - Faster than lists
2. **Safety** - Can't accidentally modify data
3. **Dictionary keys** - Tuples can be keys, lists cannot

\`\`\`python
# Using tuple as dictionary key
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
\`\`\`

## í³š Sets: Unique & Unordered

### Creating Sets

\`\`\`python
unique_words = {"cat", "dog", "cat", "bird"}
print(unique_words)  # {'cat', 'dog', 'bird'} - duplicates removed!

# Convert list to set to remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}
\`\`\`

### Set Operations

\`\`\`python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union (all elements from both)
union = set_a | set_b  # {1, 2, 3, 4, 5}

# Intersection (common elements)
intersection = set_a & set_b  # {3}

# Difference (in A but not B)
difference = set_a - set_b  # {1, 2}

# Check membership
print(3 in set_a)  # True
\`\`\`

---

## í·  ML Context

### Deduplication

\`\`\`python
# Remove duplicate labels
raw_labels = ["cat", "dog", "cat", "bird", "dog"]
unique_labels = set(raw_labels)
number_of_classes = len(unique_labels)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Tuples are immutable (like frozen lists)
âœ… Sets contain only unique elements
âœ… Use tuples for dictionary keys
âœ… Use sets to remove duplicates
âœ… Sets have union, intersection, difference operations

---
