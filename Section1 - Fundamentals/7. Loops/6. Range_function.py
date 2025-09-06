'''
The range() function in Python generates a sequence of numbers, 
which is commonly used with for loops to repeat code a specific number of times.
Create a range that starts at 0 and ends at 4:
for i in range(5):
    print(i)
This will output:
0
1
2
3
4
You can also specify a start value:
for i in range(2, 6):
    print(i)
This will output:
2
3
4
5
And you can specify a step value (increment):
for i in range(1, 10, 2):
    print(i)
This will output:
1
3
5
7
9
'''

#Challenge1:
'''
Create a function named print_range that takes three parameters:
start - the starting number (inclusive)
end - the ending number (exclusive)
step - the increment value
The function should print all numbers from start to end (not including end) with the given step increment, each on a new line.


def print_range(start, stop, step):
    for i in range(start, stop, step):
        print(i)
        pass
start = int(input())
stop = int(input())
step = int(input())
print_range(start, stop, step)

'''

#Challenge2:
'''
Create a program that performs the following tasks using range():

1. Print all numbers between 30 to 80 that are divisible by 4
2. Print the first 8 odd numbers starting from 15
3. Count backwards from 50 to 10, showing only numbers divisible by 5
4. Find the product of all numbers from 1 to 30 that are divisible by 3
When printing a number use the following code to print:

print(num, end=", ")
This will not create a new line after the number, instead it will add ,
'''


#1.Print all numbers between 30 to 80 that are divisible by 4


for i in range(30,81):
    if i % 4 == 0:
        print('Numbers between 30 to 80 that are divisible by 4 are:',i )
        
print()

#2.Print the first 8 odd numbers starting from 15

number = int(input())
for i in range(number, number+16):
    if i % 2 == 0:
        continue
    print(f'First 8 odd numbers from 15:{i}')
print()

#3.Count backwards from 50 to 10, showing only numbers divisible by 5

for num in range(50, 9, -1):
    if num % 5 == 0:
        print(f'\nCounting backwards, divisble by 5:{num}')
print()       

#4.Find the product of all numbers from 1 to 30 that are divisible by 3
product = 1
for num in range(1, 31):
    if num % 3 == 0:
        product *= num
print(f'Product of all numbers from 1 to 30 that are divisible by 3: {product}')