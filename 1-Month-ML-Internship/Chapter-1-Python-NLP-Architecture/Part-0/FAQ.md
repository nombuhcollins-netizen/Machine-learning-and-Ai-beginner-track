# Frequently Asked Questions - Part 0

## Q1: What's the difference between = and ==?

**A:** 
- `=` assigns a value to a variable
- `==` compares two values

\`\`\`python
x = 5         # Assign
x == 5        # Compare (True)
\`\`\`

## Q2: Why do I get "TypeError: can only concatenate str (not "int")?

**A:** You're trying to add strings and numbers.

\`\`\`python
# ❌ Wrong
name + " is " + age

# ✅ Right
name + " is " + str(age)
# Or
f"{name} is {age}"
\`\`\`

## Q3: What's the difference between append() and extend()?

**A:**
- `append()` adds an item (can be a list)
- `extend()` adds all items from iterable

\`\`\`python
lst = [1, 2]
lst.append([3, 4])   # [1, 2, [3, 4]]

lst2 = [1, 2]
lst2.extend([3, 4])  # [1, 2, 3, 4]
\`\`\`

## Q4: How do I check if a key exists in a dictionary?

**A:** Use `in` operator or `.get()`

\`\`\`python
d = {"name": "Alice"}

if "name" in d:
    print(d["name"])

# Or safer:
value = d.get("name", "Unknown")
\`\`\`

## Q5: Why does my list keep changing when I copy it?

**A:** You're not actually copying, just creating a reference.

\`\`\`python
# ❌ Not a copy
copy = original

# ✅ Real copy
copy = original.copy()
# Or
copy = original[:]
\`\`\`

## Q6: How do I convert a string to an integer?

**A:** Use `int()` function

\`\`\`python
age_str = "25"
age = int(age_str)
print(type(age))  # <class 'int'>
\`\`\`

# Q7: What does [::-1] do?

**A:** It reverses the sequence

\`\`\`python
text = "hello"
print(text[::-1])  # "olleh"

lst = [1, 2, 3]
print(lst[::-1])   # [3, 2, 1]
\`\`\`

---
