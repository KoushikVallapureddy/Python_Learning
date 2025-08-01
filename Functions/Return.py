'''
Return Function:
The return statement in a function is used to specify the value or values that
the function should produce as its output.
For example, the following function will output 100:
    def function_name():
        return 100
To pass the value to a variable, write:
    number = function_name()
Now the number variable will hold 100 because this is what the function returned.
'''

#Challenge1:
'''
Create a function called square_number that takes a single parameter n and returns its square. Then, call the function with the input value and store the result in a variable called result. Finally, print the value of result.

def sq(n):
    return n**2

number = int(input())
result = sq(number)
print(result)


'''


#Challenge2:
'''
Create a function called cube_number that takes a single parameter n and returns its cube. Then, call the function with the input value and store the result in a variable called result. Finally, print the value of result.
'''
    
def cube_number(n):
    return n ** 3
number = int(input())
result = cube_number(number)
print(result)
