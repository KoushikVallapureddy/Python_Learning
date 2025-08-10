'''
To convert the input to a different type, we need to cast.

To cast a string to an int (a whole number), we will write:

var = input()
var = int(var)

Or in one line,
var = int(input())

If the input is a number, i.e. 5, 4, 54 then var will hold a number. If the input contains an invalid number: 5ab, bb, akt, etc. then the program will fail.

Here is a table that shows how to cast to different types:

+---------+-------------------------------+
| Cast    | Explanation                   |
+---------+-------------------------------+
| int()   | Convert to a whole number     |
| float() | Convert to a real number      |
| bool()  | Convert to a boolean          |
| str()   | Convert to a string           |
+---------+-------------------------------+

It is important to use the right type because it can affect the output.
Adding two strings will result in:
"5" + "5" = "55"

Adding two numbers will result in:
5 + 5 = 10
'''

#Challenge:
'''
To receive multiple inputs from the user write them multiple times:
var1 = input()
var2 = input()
Every test case contains two inputs.
Store the inputs in two variables, cast them to float and print the multiplication of the two.
'''

'''
var1 = float(input('Enter the number1: '))
var2 = float(input('Enter the number2: '))

var3 = var1 * var2

print(f'{var3}')

'''

#Challenge2:
"""

Write a program that takes two inputs from the user. These inputs should be treated as numbers with decimal points.

Store the inputs in two variables, convert them to float type, and print the result of dividing the first number by the second number.

Remember, every test case will provide two inputs.

"""
'''

var1 = float(input('Enter number1: '))
var2 = float(input('Enter number2: '))
var3 = var1 / var2
print(f'{var3}')
'''


#Challenge3:
'''
Write a program that gets the user's age as input.

The program will output (print) the number of missing years till 120 (in a specific format, shown below).

For example, for input 25, the expected output is "95 years till 120".

'''
'''
var1 = int(input('Enter your age: '))
var2 = 120

var3 = var2 - var1

print(f'{var3} years till {var2}')

'''

#challenge4:

'''
Write a program that gets an input from the user, a number, 1 or 0.

The program will output "T" if the input is 1 and "F" otherwise.

Remember! you can cast the input to number using int()
'''

var1 = int(input('Enter the number: '))

if var1 == 1:
    print('T')
else:
    print('F')
