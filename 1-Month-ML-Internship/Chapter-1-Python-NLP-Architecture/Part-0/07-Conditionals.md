# 07: Conditionals - Making Decisions

**Duration:** 50 minutes | **Difficulty:** Beginner | **Key Skill:** Control flow with if/elif/else

---

## í¾¯ What You'll Learn

- if, elif, else statements
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Nested conditionals

---

## í³š Core Concept: Conditionals

Conditionals allow your code to make decisions based on conditions.

### Basic If-Elif-Else

\`\`\`python
age = 25

if age >= 65:
    print("Retire")
elif age >= 18:
    print("Adult")
else:
    print("Minor")
# Output: Adult
\`\`\`

### Comparison Operators

\`\`\`python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a <= b)   # True
print(a > b)    # False
print(a >= b)   # False
\`\`\`

### Logical Operators

\`\`\`python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

score = 55
if score >= 90 or score >= 80:
    print("Pass")

if not (score < 60):
    print("Passed")
\`\`\`

---

## í·  ML Context

### Data Validation

\`\`\`python
value = 0.95

if 0 <= value <= 1:
    print("Valid probability")
else:
    print("Invalid probability")
\`\`\`

---

## í´‘ Key Takeaways

âœ… Use if/elif/else for decision making
âœ… Comparison operators: ==, !=, <, >, <=, >=
âœ… Logical operators: and, or, not
âœ… Indentation matters in Python!

---
