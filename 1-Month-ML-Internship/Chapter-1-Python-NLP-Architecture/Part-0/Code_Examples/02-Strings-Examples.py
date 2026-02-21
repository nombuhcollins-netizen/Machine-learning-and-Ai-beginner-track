# String Examples

text = "Python Programming"

# Indexing
print(text[0])      # 'P'
print(text[-1])     # 'g'

# Slicing
print(text[0:6])    # 'Python'
print(text[7:])     # 'Programming'
print(text[::-1])   # Reverse

# String methods
print(text.lower())     # 'python programming'
print(text.upper())     # 'PYTHON PROGRAMMING'
print(text.split())     # ['Python', 'Programming']

# F-strings (formatting)
name = "Bob"
age = 35
print(f"{name} is {age} years old")

# Strip whitespace
text = "  hello world  "
print(text.strip())  # 'hello world'
