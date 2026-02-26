# Intermediate Exercises - Part 0
# 1. Lists (From Lesson 4)
#Exercise 1: List Operations

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# Sort the list
numbers_sorted = numbers.sort()
#Find max and min
print(max(numbers))
print(min(numbers))
#Count occurrences of 1
numbers_of_ones = numbers.count(1)
# Remove all 1s
print(numbers.remove(1))
#Calculate average
avg = sum(numbers)/len(numbers)

#Exercise 2: Slicing Practice
data = [10, 20, 30, 40, 50, 60, 70]
# Get every 2nd element
data_2nd_elt = data[::2]
#Get last 3 elements
last_3_elts = data[-3]
#Reverse the list using slicing
rev_list = data[::-1]

#Exercise 3: Data Normalization
scores = [55, 65, 75, 85, 95]
#Normalize to 0-1 range and print.


## 2. Dictionaries (From Lesson 5)
#Exercise 4: Student Dictionary
#Create dict with name, age, gpa. Update gpa, print all keys.
student_dict = {'name': 'jane', 'age': 18, 'gpa': 4.0}

#Exercise 5: Frequency Counter
text = "the quick brown fox"
words = text.split()
#Create dict counting each word frequency.
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)
#Exercise 6: Config Manager
#Create ML config dict with lr, epochs, batch_size. Print values.


## 3. Conditionals & Loops (From Lessons 7-8)
#Exercise 7: Grade Classifier
#Read grade (0-100), print A/B/C/D/F.

#Exercise 8: Loop Pattern
'''Print this pattern:
*
**
***
****
*****'''
num = int(input('enter your limit: '))
for row in range(num):
    print()
    for column in range(row):
        print('*', end=' ' )
    
#Exercise 9: Even/Odd Separator
#Separate list of numbers into evens and odds.
num = [x for x in range(20)]
print(num)
even_num = [i for i in range(20) if i % 2 == 0 ]
print(even_num)
odd_num = [j for j in range(20) if j % 2 != 0 ]
print(odd_num)

