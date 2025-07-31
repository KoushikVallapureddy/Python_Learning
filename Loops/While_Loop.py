'''
A while loop is different from the for loop. A for loop allows us to iterate over a specific range, whereas a while loop allows us to keep iterating as long as a certain condition is met.
To use while loop write:
while condition:
    code
The code will execute only if the condition is true.
There are many use cases where a while would solve the problem, but the for loop would not. 

For example consider this problem:
Find the smallest power of 2 that is greater than a given number.
To solve it we will use a while loop that will repeatedly multiply the current power of 2 by 2 until it becomes greater than the given number:

number = 27
power_of_two = 1

while power_of_two <= number:
    power_of_two *= 2
print(power_of_two)

'''
#Challenge1:
'''
Write a program that gets one input, float number.

Use a while loop to divide the input by 2 as long as the number is bigger or equal to 3.5.

Print the first number that is smaller than 3.5.
'''

var = float(input())
while var >= 3.5:
    var /= 2
print(var)
