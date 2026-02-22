"""
Solutions for Exercise Set 2: Advanced Python Patterns
"""

import time
from functools import wraps

# ===== BEGINNER SOLUTIONS =====

def timer(func):
    """Decorator that measures execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

def fibonacci_gen(n):
    """Generator yielding fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# ===== INTERMEDIATE SOLUTIONS =====

def validate_input(**type_checks):
    """Decorator for input validation"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for key, expected_type in type_checks.items():
                if key in kwargs and not isinstance(kwargs[key], expected_type):
                    raise TypeError(f"{key} must be {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class FileReader:
    """Context manager for file reading"""
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# ===== ADVANCED SOLUTIONS =====

def retry(max_attempts=3):
    """Decorator for retrying failed functions"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed, retrying...")
        return wrapper
    return decorator

def pipeline_generator(batches):
    """Generator for processing ML pipeline steps"""
    for batch in batches:
        processed = [x * 2 for x in batch]
        yield processed

if __name__ == "__main__":
    @timer
    def slow_function():
        time.sleep(0.1)
    
    slow_function()
    
    for fib in fibonacci_gen(5):
        print(fib)
