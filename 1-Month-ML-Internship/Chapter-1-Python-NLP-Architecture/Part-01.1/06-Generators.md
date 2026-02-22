# 06: Generators - Memory-Efficient Iteration

**Duration:** 50 minutes | **Difficulty:** Advanced | **Key Skill:** Iterator protocol

---

## í¾¯ What You'll Learn

- Generator functions
- yield statement
- Generator expressions
- Memory efficiency

---

## í³š Generators

### Generator Function

\`\`\`python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
    i += 1

for num in count_up_to(3):
    print(num)  # 1, 2, 3
\`\`\`

### ML Context: Batch Processing

\`\`\`python
def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]

for batch in batch_generator([1,2,3,4,5], 2):
    print(batch)  # [1,2], [3,4], [5]
\`\`\`

---

## í´‘ Key Takeaways

âœ… Generators lazy-load data
âœ… Memory-efficient for large datasets
âœ… yield pauses execution
âœ… Essential for ML data pipelines

---
