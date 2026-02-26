# 01-Variables-Exercises.py
# Practice exercises for Variables and Data Types
# Exercise 1: Type Checking
numbers = [25, 19.99, "hello", True, None]
# Print the type of each value
for number in numbers:
    print(f'{number}: {type(number)}')
# Exercise 2: Type Conversion
# Convert these to appropriate types:
age_str = "30"
price = 99.99
is_valid = "True"

age_int = int(age_str)
price2 = int(price)
is_valid2 = bool(is_valid)

# Exercise 3: ML Data Setup
# Create variables for:
# - Model accuracy (float between 0-1)
# - Number of samples (integer)
# - Dataset name (string)
# - Is training complete (boolean)

# Exercise 4: Data Validation
def validate_probability(value):
    # Return True if 0 <= value <= 1, else False
    if value >= 0 and value <=1 :
        return True
    else:
        return False
        


# Test your function
test_values = [0.5, -0.1, 1.5, 0, 1]
for val in test_values:
    result = validate_probability(val)
    print(f"{val}: {result}")