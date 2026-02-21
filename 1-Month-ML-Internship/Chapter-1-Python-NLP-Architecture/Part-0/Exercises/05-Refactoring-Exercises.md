# Code Refactoring Exercises - Part 0

Learn to write better code!

## Exercise 1: Make it Pythonic

**Original (❌ Bad):**
\`\`\`python
i = 0
result = []
while i < len(numbers):
    if numbers[i] > 10:
        result.append(numbers[i] * 2)
    i += 1
\`\`\`

**Refactored (✅ Good):**
\`\`\`python
result = [x * 2 for x in numbers if x > 10]
\`\`\`

## Exercise 2: Extract Function

**Original (❌ Monolithic):**
\`\`\`python
# Entire processing in one function
def process_data(data):
    # 50 lines of code
    pass
\`\`\`

**Refactored (✅ Modular):**
\`\`\`python
def load_data(filename):
    pass

def clean_data(data):
    pass

def normalize_data(data):
    pass

def process_data(filename):
    data = load_data(filename)
    data = clean_data(data)
    data = normalize_data(data)
    return data
\`\`\`

## Exercise 3: Add Error Handling

Add try-except blocks to make code robust.

## Exercise 4: Improve Readability

- Add docstrings
- Improve variable names
- Add comments where needed
- Follow naming conventions

---
