# Part 0 Quick Reference Guide

## Variables & Types

\`\`\`python
name = "Alice"          # String
age = 25               # Integer
height = 1.75          # Float
is_ready = True        # Boolean
none_val = None        # NoneType

print(type(name))      # Check type
\`\`\`

## String Operations

\`\`\`python
text = "Python"
text[0]                # "P"
text[0:3]              # "Pyt"
text.lower()           # "python"
text.upper()           # "PYTHON"
text.strip()           # Remove whitespace
text.replace("n", "x") # "Pythox"
text.split()           # Split into list
" ".join(["a", "b"])   # Join list
\`\`\`

## Collections

\`\`\`python
# Lists (mutable)
lst = [1, 2, 3]
lst.append(4)
lst[0]
lst[1:3]

# Dictionaries
dct = {"name": "Alice", "age": 25}
dct["name"]
dct["job"] = "Engineer"

# Tuples (immutable)
tup = (1, 2, 3)
tup[0]

# Sets (unique)
st = {1, 2, 3}
st.add(4)
\`\`\`

## Loops

\`\`\`python
# For loop
for i in range(5):
    print(i)

for item in [1, 2, 3]:
    print(item)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
\`\`\`

## Functions

\`\`\`python
def greet(name="Friend"):
    return f"Hello, {name}!"

result = greet("Alice")
\`\`\`

## Conditionals

\`\`\`python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
\`\`\`

---
