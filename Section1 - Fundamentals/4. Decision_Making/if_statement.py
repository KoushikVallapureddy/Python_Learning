'''
if statement allows us to execute code with conditions. 
To use an if statement, we need to add a colon (:) at the end of the if, and everything that is inside the if is indented with 4 spaces or a tab.
If the condition is true, the code inside the if block will be executed.
'''

#Challenge 1:
'''
The variables a and b have missing values, fill them so that the code inside the if statement will be executed! (make sure the if condition is true)

At the end of the program, the value of c should be 3.
'''
'''
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
c = 0
if a >= b and b > 10:
    c = 2
c += 1

print(f'The value of c is: = {c}')
'''

#Challenge 2: 

"""
The variables a and b. Fill them so that the code inside the if statement will be executed! (make sure the if condition is true)

At the end of the program, the value of c should be 3.
"""

a = int(input('enter the value of a: '))
b = int(input('enter the value of b: ')) 
c = 0
if a < b or b >= 10:
    c = 2
c += 1
print(f'the value of c is: = {c}')






