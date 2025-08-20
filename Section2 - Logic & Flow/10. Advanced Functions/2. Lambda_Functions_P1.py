'''
Lambda Functions part1:
A lambda function is a small, anonymous function defined using the lambda keyword. 
Lambda functions can take any number of arguments but can only have one expression. 
They are useful for creating simple, one-line functions without the need for a full function definition using the def keyword.

The syntax of a lambda function is:
    lambda arguments: expression

Here's a breakdown of the syntax:
    lambda: The keyword that indicates the start of a lambda function definition.
    arguments: A comma-separated list of arguments, similar to the parameters in a regular function definition.
    expression: A single expression that is evaluated and returned as the result of the lambda function.

Here's an example of a lambda function that adds two numbers:
    add = lambda x, y: x + y
    result = add(5, 3)
    print(result)
    # Output: 8

In this example, the lambda function takes two arguments, x and y, and returns their sum. 
The lambda function is assigned to the variable add, which can then be called like a regular function.

Lambda functions are often used in situations where a short, throwaway function is needed, such as with higher-order functions like map, filter, and reduce.
'''

#Challenge1:
'''
Create a lambda function named multiply that takes three arguments, x, y, and z, and returns their product. 
After defining the lambda function, call it with the values 2, 3, and 4, and print the result.
'''
mutiply = lambda x, y, z : x * y * z
result = mutiply(2,3,4)
print(result)

#Challenge2:
'''
Create a lambda function named average that takes four arguments, a, b, c, and d, and returns their average (mean). 
After defining the lambda function, call it with the values 10, 15, 20, and 25, and print the result.
'''

average = lambda a,b,c,d:(a+b+c+d)/4
result = average(10,15,20,25)
print(result)