# 01: Variables & Data Types

**Duration:** 45 minutes | **Difficulty:** Beginner | **Key Skill:** Understanding Python's type system

---

## 🎯 What You'll Learn

- What variables are and how to create them
- Python's main data types: int, float, bool, str, None
- Type checking and conversion
- Naming conventions
- ML Context: Why data types matter for machine learning

---

## 📚 Core Concept: Variables & Data Types

A **variable** is a container for storing data values. In Python, variables don't need to be explicitly typed—Python automatically determines the type based on the value assigned.

### The Four Essential Data Types

| Type | Purpose | Example | ML Use |
|------|---------|---------|--------|
| `int` | Whole numbers | `5`, `-10`, `0` | Counts, indices, dimensions |
| `float` | Decimal numbers | `3.14`, `-0.5` | Probabilities, weights, scores |
| `str` | Text | `"hello"`, `'world'` | Text data, labels, NLP |
| `bool` | True/False | `True`, `False` | Flags, conditions, masks |

---

## 💻 Creating & Using Variables

### Basic Variable Assignment

```python
# Integer - whole numbers
age = 25
year = 2026
count = -10

# Float - decimal numbers
price = 19.99
probability = 0.95
temperature = -273.15

# String - text
name = "Alice"
greeting = 'Hello, World!'
message = """This is a
multi-line string"""

# Boolean - True or False
is_student = True
has_experience = False
is_ready = True
```

### Variable Names - Conventions

```python
# ✅ GOOD variable names
age = 30
user_name = "Bob"
max_value = 100
is_active = True
NUM_ITERATIONS = 1000  # Constants in ALL_CAPS

# ❌ BAD variable names - avoid these
x = 30              # Too vague
a = "Bob"           # Not descriptive
max-value = 100     # Hyphens not allowed
2val = 50           # Can't start with number
class = 'Student'   # 'class' is a reserved word
```

**Best Practices:**
- Use descriptive names that explain what the variable stores
- Use lowercase with underscores for regular variables: `student_age`
- Use UPPERCASE for constants: `MAX_RETRIES`
- Avoid Python keywords: `class`, `def`, `return`, `if`, `for`, etc.

---

## 🔍 Checking Data Types

Use the `type()` function to check what type a variable is:

```python
age = 25
print(type(age))              # <class 'int'>

price = 19.99
print(type(price))            # <class 'float'>

name = "Alice"
print(type(name))             # <class 'str'>

is_ready = True
print(type(is_ready))         # <class 'bool'>

nothing = None                # Special "no value" type
print(type(nothing))          # <class 'NoneType'>
```

---

## 🔄 Type Conversion

Converting between types is essential for data processing:

```python
# String to Integer
score_str = "95"
score_int = int(score_str)
print(score_int)              # 95 (now a number)
print(type(score_int))        # <class 'int'>

# Integer to String
count = 42
count_str = str(count)
print(count_str)              # "42" (now text)

# Float to Integer (truncates decimal)
price = 19.99
price_int = int(price)
print(price_int)              # 19 (decimal removed)

# String to Float
temperature_str = "98.6"
temperature = float(temperature_str)
print(temperature)            # 98.6

# To Boolean (be careful!)
print(bool(1))                # True (any non-zero is True)
print(bool(0))                # False (zero is False)
print(bool(""))               # False (empty string is False)
print(bool("hello"))          # True (non-empty string is True)
```

---

## ⚠️ Common Data Type Pitfalls

### Pitfall 1: String vs Number

```python
# This looks like a number but it's text!
age = "25"            # This is a STRING ("25")
actual_age = 25       # This is an INT (25)

print(type(age))      # <class 'str'>
print(type(actual_age))  # <class 'int'>

# You can't do math with strings!
# print(age + 5)  # ❌ ERROR: can't add int to str

# You need to convert first
print(int(age) + 5)   # ✅ 30 (works!)
```

### Pitfall 2: Float Precision

```python
# Floats can have precision issues
result = 0.1 + 0.2
print(result)         # 0.30000000000000004 (not exactly 0.3)

# Solution: Round when needed
rounded = round(result, 2)
print(rounded)        # 0.3
```

### Pitfall 3: Comparing Different Types

```python
print(5 == "5")       # False (int vs str)
print(5 == 5.0)       # True (int vs float, both equal)
print(True == 1)      # True (bool 1 is same as int 1)
print(False == 0)     # True (bool 0 is same as int 0)
```

---

## 🧠 ML Context: Why This Matters

### Data Type Selection in ML

**Integers** → Labels, counts, indices
```python
# In ML, you might have label encoding
label = 0  # class 0 (cat)
label = 1  # class 1 (dog)
count = 100  # 100 samples
```

**Floats** → Model predictions, weights, probabilities
```python
# Model output is typically float
prediction = 0.95  # 95% confidence
weight = -0.42     # Neural network weight
probability = 0.75 # Probability of class
```

**Strings** → Text data (critical for NLP!)
```python
# Raw text before processing
text = "Machine learning is fascinating!"
label = "positive"  # sentiment label
```

**Booleans** → Flags and conditions
```python
# Is this data point valid?
is_valid = True
# Should we preprocess this text?
needs_cleaning = False
```

---

## 📝 Exercises

### Try It! (Quick Checks)

**Exercise 1.1: Create Variables**
```python
# Create variables for the following and print their types:
# - Your age
# - Your height in meters (as decimal)
# - Your name
# - Whether you like pizza (True/False)
```

**Exercise 1.2: Type Checking**
```python
# What type is each of these?
a = 10
b = 10.0
c = "10"
d = True

# Can you explain why b and d == 1 but a != c?
```

**Exercise 1.3: Type Conversion**
```python
# Convert string "100" to integer and add 50
# Convert integer 42 to string and print "I am 42 years old"
# Convert "3.14" to float
```

### Do It! (Hands-on Practice)

**Exercise 1.4: Temperature Converter**
```python
# You have a temperature in Celsius as a string: "25.5"
# 1. Convert it to a float
# 2. Convert to Fahrenheit: F = (C * 9/5) + 32
# 3. Print the result with the type

celsius_str = "25.5"
# Your code here
# Expected: 77.9 degrees Fahrenheit
```

**Exercise 1.5: Data Validation**
```python
# Given these values, check their types and determine if they're valid for:
# - A price (should be float > 0)
# - A name (should be non-empty string)
# - A count (should be positive int)

value1 = 19.99
value2 = "Alice"
value3 = 5

# Your code here - print "Valid" or "Invalid" for each
```

### Master It! (Challenges)

**Exercise 1.6: Guess the Type**
```python
# Without running the code, determine the type of each result:
result1 = int("42")
result2 = str(3.14)
result3 = bool("False")  # Hint: This will surprise you!
result4 = float(5)
result5 = "5" + "5"

# Run your predictions, then check!
```

**Exercise 1.7: ML Data Setup**
```python
# Simulate preparing ML training data:
# You have raw data that needs type conversion:

image_count = "1000"        # String from user input
accuracy_score = 0.92       # Float from model
is_labeled = "True"         # String from database
batch_size = 32             # Integer

# 1. Convert image_count to integer
# 2. Verify accuracy_score is float
# 3. Convert is_labeled to boolean
# 4. Print all with their types

# Print in format: "image_count: 1000 (int)"
```

---

## 🎬 Code-Along Example

```python
# Let's build a simple student profile

# Creating variables for a student
student_name = "Emma"
student_id = 12345
gpa = 3.85
is_honors = True
major = "Computer Science"

# Printing the profile
print("=" * 40)
print("STUDENT PROFILE")
print("=" * 40)
print(f"Name: {student_name}")
print(f"ID: {student_id}")
print(f"GPA: {gpa}")
print(f"Honors Student: {is_honors}")
print(f"Major: {major}")
print("=" * 40)

# Type information
print("\nData Types:")
print(f"name type: {type(student_name)}")
print(f"id type: {type(student_id)}")
print(f"gpa type: {type(gpa)}")
print(f"honors type: {type(is_honors)}")
```

Expected output:
```
========================================
STUDENT PROFILE
========================================
Name: Emma
ID: 12345
GPA: 3.85
Honors Student: True
Major: Computer Science
========================================

Data Types:
name type: <class 'str'>
id type: <class 'int'>
gpa type: <class 'float'>
honors type: <class 'bool'>
```

---

## 🔑 Key Takeaways

✅ Variables store data in memory  
✅ Python has 4 main types: int, float, str, bool (plus None)  
✅ Check types with `type()`  
✅ Convert between types with `int()`, `float()`, `str()`, `bool()`  
✅ Use descriptive variable names  
✅ Understand type conversion for data preprocessing  

---

## 🚀 Next: [02-Strings](./02-Strings.md)

Strings are crucial for text processing in ML/NLP. Learn powerful string operations!

---

## 📚 Additional Resources

- [Python Data Types - Official Docs](https://docs.python.org/3/tutorial/introduction.html)
- [Type Casting in Python](https://www.w3schools.com/python/python_casting.asp)
