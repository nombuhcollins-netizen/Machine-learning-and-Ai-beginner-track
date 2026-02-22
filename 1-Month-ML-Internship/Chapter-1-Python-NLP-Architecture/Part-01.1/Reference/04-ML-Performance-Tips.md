# ML Performance Optimization Tips

## Profiling
- Use `cProfile` for detailed analysis
- Use `timeit` for quick comparisons
- Profile before optimizing

## Memory Efficiency
- Use generators for large datasets
- Use `__slots__` for memory-heavy classes
- Delete large objects when done

## Speed Optimization
- List comprehensions > loops
- NumPy operations > Python loops
- Use appropriate data structures

## Big O Complexity
- O(1) - constant
- O(n) - linear
- O(n²) - quadratic
- O(log n) - logarithmic

## ML-Specific
- Batch processing for datasets
- Vectorization with NumPy
- Cache computed results
