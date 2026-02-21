# 05: Dictionaries - Key-Value Data Storage

**Duration:** 50 minutes | **Difficulty:**  Beginner | **Key Skill:** Mapping and data associations

---

## ÌæØ What You'll Learn

- Creating and accessing dictionaries
- Dictionary methods (.keys(), .values(), .items())
- Adding, modifying, and deleting key-value pairs
- Iterating through dictionaries
- ML Context: Storing labeled data and configurations

---

## Ì≥ö Core Concept: Dictionaries

A **dictionary** is a collection of key-value pairs. Unlike lists (accessed by index), dictionaries are accessed by keys.

### Creating Dictionaries

\`\`\`python
# Empty dictionary
empty_dict = {}

# Dictionary with data
student = {
    "name": "Alice",
    "age": 25,
    "gpa": 3.85
}

# Access values
print(student["name"])  # "Alice"
print(student["age"])   # 25
\`\`\`

### Dictionary Keys Must Be Unique

\`\`\`python
# Keys are unique
config = {
    "learning_rate": 0.01,
    "epochs": 100,
    "batch_size": 32
}

# Change a value
config["epochs"] = 50  # Now 50

# Add new key-value pair
config["model"] = "neural_network"
\`\`\`

## Essential Dictionary Methods

\`\`\`python
user = {"name": "Bob", "age": 30, "city": "NYC"}

# Get all keys
keys = user.keys()     # dict_keys(['name', 'age', 'city'])

# Get all values
values = user.values() # dict_values(['Bob', 30, 'NYC'])

# Get all key-value pairs
items = user.items()   # [('name', 'Bob'), ('age', 30), ...]

# Get value with default if key missing
age = user.get("age", 0)    # 30
job = user.get("job", "Unknown")  # "Unknown"

# Update with another dictionary
user.update({"age": 31, "job": "Engineer"})

# Remove item
del user["city"]  # or user.pop("city")
\`\`\`

## Ì¥Ñ Iterating Through Dictionaries

\`\`\`python
person = {"name": "Charlie", "age": 28, "job": "Data Scientist"}

# Iterate over keys
for key in person:
    print(key)

# Iterate over keys and values
for key, value in person.items():
    print(f"{key}: {value}")
\`\`\`

## Ì∑† ML Context: Using Dictionaries

### Configuration Storage

\`\`\`python
# Model hyperparameters
config = {
    "learning_rate": 0.001,
    "batch_size": 64,
    "epochs": 100,
    "optimizer": "adam"
}
\`\`\`

### Label Mapping

\`\`\`python
# Map labels to IDs
label_to_id = {
    "positive": 1,
    "negative": 0,
    "neutral": 2
}

# Reverse mapping
id_to_label = {v: k for k, v in label_to_id.items()}
\`\`\`

---

## Ì≥ù Exercises

### Try It! (Quick Checks)

**Exercise 5.1: Basic Dictionary**
\`\`\`python
# Create a dictionary for a book with: title, author, pages, published_year
\`\`\`

**Exercise 5.2: Accessing Dictionary**
\`\`\`python
product = {"name": "Laptop", "price": 999, "stock": 5}

# 1. Access the price
# 2. Add a "discount" key with value 10
# 3. Get all keys
\`\`\`

### Do It! (Hands-on Practice)

**Exercise 5.3: Frequency Counter**
\`\`\`python
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# Create a dictionary counting word frequency
# Hint: For each word, if in dict, increment count; else add with count 1
\`\`\`

### Master It! (Challenges)

**Exercise 5.4: ML Dataset Parser**
\`\`\`python
# Parse a simple CSV-like data into list of dictionaries
data_lines = [
    "name,age,score",
    "Alice,25,95",
    "Bob,23,87",
    "Charlie,26,92"
]

# Create list of dicts: [{"name": "Alice", ...}, ...]
\`\`\`

---

## Ì¥ë Key Takeaways

‚úÖ Dictionaries use key-value pairs for flexible data storage
‚úÖ Keys must be unique; values can repeat
‚úÖ Access values with dict[key] or dict.get(key)
‚úÖ Use .keys(), .values(), .items() for iteration
‚úÖ Essential for storing configurations and mappings in ML

---
