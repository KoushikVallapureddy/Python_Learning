'''
Break: 
The break statement stops the loop instantly when it's encountered.
for example,
for i in range(10):
    if i == 6
        break
    print(i)
In the following example the loop iterates regularly until it reaches number 6. 
Then the program enters the if statement and executes the break statement. This exits the loop immediately. The output is:
0
1
2
3
4
5

'''
#Challenge1:
'''
You are given a code that prints the numbers from 1 to 10 (including).
Your task is to add if and break statements so that only the numbers from 1 to 5 will be printed, 
the loop will exit before printing the numbers from 6 to 10.


for i in range(1,11):
    if i == 6:
        break
    print(i)

'''

#Challenge2:
'''
Write a program that:
Takes two numbers as input
Creates a list of numbers from the first input to the second input (not including)
Finds and prints the first even number greater than 5
Then, in a separate loop, find and print the first number divisible by 7
Output the result in the following format:
    First even number greater than 5: [...]
    First number divisible by 7: [...]
'''

number1 = int(input())
number2 = int(input())
for i in range(number1, number2):
    if i % 2 == 0 and i > 5:
        print(f'First even number greater than 5: {i}')
        break


for i in range(number1, number2):
    if i % 7 == 0:
        print(f'First number divisble by 7: {i}')
        break
    
        

