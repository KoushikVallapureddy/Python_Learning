'''
Arguments:
An argument in a function is a value that you pass into the function when you call it. 
To add arguments to a function, we write them inside the parenthesis ():
    def function_name(arg1, arg2, ...):
    code
We can name the arguments as we want, and we can write as many arguments as we need.
To call a function and pass arguments to it, we write:
    function_name(value1, value2, value3, ...)
Passing too many arguments to a function that is expecting less arguments will cause the program to fail

Example of usage:
    def is_even(number):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    for i in range(15, 34):
        is_even(i)
    for i in range(153, 219):
        is_even(i)  

Here we have a function called is_even that accepts one argument called number and prints if the number is even or odd. 
Then we call the function twice:one time for all the numbers between 15 and 34, and the second time for all the numbers between 153 and 219.  
'''
