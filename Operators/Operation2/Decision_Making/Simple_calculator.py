'''
You are given a code which gets as input two numbers n1 and n2 and a character op.

The possible values for op are '+', '-', '/' and '*'

Your task is to set the variable result based on the conditions:

if op is '+', set result with n1 + n2.
if op is '-', set result with n1 - n2.
if op is '/', set result with n1 / n2.
if op is '*', set result with n1 * n2.
'''

num1 = int(input('enter number1: '))
num2 = int(input('enter number2: '))
operation = input('operator is: ')
result = 0

if operation == '+' :
    result = num1 + num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1*num2
elif operation == '/':
    result = num1/num2
else:
    result = "Invalid Operation"

print(f'result = {result}')

