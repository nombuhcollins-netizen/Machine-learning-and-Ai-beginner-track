# 08: Loops - Repeating Code

**Duration:** 50 minutes | **Difficulty:** Beginner | **Key Skill:** Iteration patterns

---

## í¾¯ What You'll Learn

- for loops (iterating over sequences)
- while loops (condition-based repetition)
- break and continue statements
- range() function
- Nested loops

---

## í³š For Loops

### Basic For Loop

\`\`\`python
# Iterate over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char)
\`\`\`

### Using range()

\`\`\`python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
\`\`\`

### Break & Continue

\`\`\`python
# break - exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
\`\`\`

## í³š While Loops

\`\`\`python
# Repeat while condition is True
count = 0
while count < 3:
    print(count)
    count += 1

# Infinite loop (be careful!)
# while True:
#     print("This repeats forever")
#     break  # Need a way to exit
\`\`\`

---

## í·  ML Context

### Processing Dataset

\`\`\`python
scores = [85, 92, 78, 95, 88]

total = 0
for score in scores:
    total += score

average = total / len(scores)
print(f"Average: {average}")
\`\`\`

---

## í´‘ Key Takeaways

âœ… for loops iterate over sequences
âœ… while loops repeat based on conditions
âœ… break exits loop early
âœ… continue skips to next iteration
âœ… range(start, stop, step) generates sequences
âœ… Loops are essential for processing datasets

---
