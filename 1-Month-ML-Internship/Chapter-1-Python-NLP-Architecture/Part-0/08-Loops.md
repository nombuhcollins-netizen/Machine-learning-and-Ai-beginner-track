# 08: Loops - Repeating Code

**Duration:** 50 minutes | **Difficulty:** Beginner | **Key Skill:** Iteration with for and while

---

## í¾¯ What You'll Learn

- for loops
- while loops
- break and continue
- range() function

---

## í³š For Loops

### Basic For Loop

\`\`\`python
# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop through a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
\`\`\`

### range() Function

\`\`\`python
range(5)           # 0, 1, 2, 3, 4
range(2, 5)        # 2, 3, 4
range(0, 10, 2)    # 0, 2, 4, 6, 8
\`\`\`

## í³š While Loops

\`\`\`python
count = 0
while count < 5:
    print(count)
    count += 1
\`\`\`

## í´„ Break & Continue

\`\`\`python
# Break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue - skip this iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
\`\`\`

---

## í·  ML Context

### Processing Datasets

\`\`\`python
# Train model
epochs = 100
for epoch in range(epochs):
    # Train...
    loss = calculate_loss()
    if loss < threshold:
        break
\`\`\`

---
