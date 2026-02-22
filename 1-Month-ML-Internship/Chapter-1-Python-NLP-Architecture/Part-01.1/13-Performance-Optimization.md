# 13: Performance Optimization - Profiling and Speed

**Duration:** 60 minutes | **Difficulty:** Advanced | **Key Skill:** Optimization

---

## í¾¯ What You'll Learn

- Profiling techniques
- Big O complexity
- Optimization strategies
- Benchmarking code

---

## í³š Performance Analysis

### Timing Code

\`\`\`python
import time

def slow_func():
    return sum([i**2 for i in range(10000)])

start = time.time()
result = slow_func()
elapsed = time.time() - start
print(f"Time: {elapsed:.4f}s")
\`\`\`

### Using cProfile

\`\`\`python
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

cProfile.run('fibonacci(30)')
\`\`\`

---

## í´‘ Key Takeaways

âœ… Profile before optimizing
âœ… Understand Big O complexity
âœ… Use generators for memory efficiency
âœ… Critical for ML at scale

---
