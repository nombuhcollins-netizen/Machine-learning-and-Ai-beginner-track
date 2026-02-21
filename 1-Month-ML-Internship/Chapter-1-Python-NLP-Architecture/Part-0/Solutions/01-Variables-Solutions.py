# 01-Variables-Solutions.py - SOLUTIONS

# Solution 1: Type Checking
values = [25, 19.99, "hello", True, None]
for val in values:
    print(f"{val}: {type(val)}")

# Solution 2: Type Conversion
age = int("30")
price = 99.99
is_valid = "True" == "True"

# Solution 3: ML Data Setup
accuracy = 0.95
samples = 1000
dataset_name = "training_data_v1"
training_complete = True

# Solution 4: Validation
def validate_probability(value):
    return 0 <= value <= 1

for val in [0.5, -0.1, 1.5, 0, 1]:
    print(f"{val}: {validate_probability(val)}")
