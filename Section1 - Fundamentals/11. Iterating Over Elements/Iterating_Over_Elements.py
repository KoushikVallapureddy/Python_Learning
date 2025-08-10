'''
Iterating Over Elements:
Iteration means going through elements one by one in a sequence. 
With lists, we can access each element systematically using different methods.
The most common way to iterate through a list is using a for loop:
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(fruit)
Output:
    apple
    banana
    orange
'''

#Challenge1:
'''
Create a program that receives a list as input (given), and prints a new list containing only the words longer than 5 characters


lst = input().split(",")
result = []
for word in lst:
    if len(word.strip()) > 5:
        result.append(word.strip())
print(result)

'''

#Challenge2:
'''
Create a program that receives a list of numbers as input (given), and prints the sum of all even numbers in the list.
'''

numbers = input().split(',')
total = 0
for num in numbers:
    if int(num.strip()) % 2 == 0:
        total += int(num.strip())
print(total)

