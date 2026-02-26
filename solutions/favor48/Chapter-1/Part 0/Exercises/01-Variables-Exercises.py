# Exercise 1: Type Checking(Print the type of each value)
values = [25, 19.99, "hello", True, None]
for val in values:
    print(f"{val}: {type(val)}")


# Exercise 2: Type Conversion(Convert these to appropriate types)
age_str = "30"
price = 99.99
is_valid = "True"
age = int(age_str)
price_int = int(price)
is_valid_bool = is_valid.lower() == "true"
print(type(age), age)
print(type(price_int), price_int) 
print(type(is_valid_bool), is_valid_bool)


# Excercise 3: ML Data Setup
model_accuracy = 0.95
number_of_samples = 1000
dataset_name = "training_data"
is_training_complete = True


# Exercise 4: Validation
def validate_probability(value):
    #Return True if 0 <= value, else False
   if 0 <= value <= 1:
       return True
   else:
       return False
#Test your function
test_values = [0.5, -0.1, 1.5, 0, 1]
for val in test_values:
    result = validate_probability(val)
    print(f"{val}: {result}")

