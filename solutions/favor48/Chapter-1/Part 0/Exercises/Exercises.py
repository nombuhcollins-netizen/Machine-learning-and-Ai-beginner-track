# 01-Beginner Exercise - Part 0

## Exercise 1: Profile Creator
name = "Favor"
age = 18
height = 1.6
is_student = True

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is student: {is_student}, Type: {type(is_student)}")


## Exercise 2: Type Challenge
a = "10"
b = 10
c = 10.0

print(type(a))  
print(type(b))  
print(type(c))  
# Can't add a + b (because we cannot add str + int)
# Can add b + c (because we can add int + float = float)
 

## Exercise 3: Conversion
age_str = input("Enter your age: ")
age = int(age_str)
future_age = age + 10
print(f"In 10 years, you will be {future_age}")


## Exercise 4: Text Processing
text = "  Hello, World! HELLO  "

text = text.strip()
print(text)  

text = text.lower()
print(text)  

count = text.count("hello")
print(count)  

text = text.replace("world", "python")
print(text)  


# Exercise 5: Slicing(finding the file extension of "document.pdf")
file = "document.pdf"
extension = file.split(".")[-1]
print(extension)


#Exercise 6: Email Validation(Checking if an email contains "@") and ends wit ".com"
email = input("Enter email: ")
if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")


#Excercise 7: Calculator(read 2 numbers, perform +,-,*,/ and print)
num1 = float(input("Num1: "))
num2 = float(input("Num2: "))

print("Sum:", num1 + num2)
print("Diff:", num1 - num2)
print("Product:", num1 * num2)
if num2 != 0:
    print("Div:", num1 / num2)
else:
    print("Cannot divide by zero!")


#Exercise 8: Temperature(convert 25C to F=(C*9/5)+32)
celsuis = 25
fahrenheit = (celsuis * 9/5) + 32
print(f"{celsuis}C = {fahrenheit}F")


#Exercice 9: Percentage(calculate what percentage 25 is of 200)
part = 25
whole = 200
percentage = (part / whole) * 100
print(f"{part} is {percentage}% of {whole}")