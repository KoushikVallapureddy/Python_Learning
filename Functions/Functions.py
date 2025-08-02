'''
Declare a Function:
A function is a sequence of code that has a name. The purpose of a function is to reuse a piece of code multiple times.
For example, take a look at this code:
print("Welcome to Coddy")
print("New session...")
print("Welcome to Coddy")
print("Another session...")
print("Welcome to Coddy")

We use the same code print("Welcome to Coddy") over and over again. 
Another issue with this code is that if we wanted to change the message:
Welcome to Coddy to something different, like "Welcome aboard" it would have to change 3 different lines of code. 
To solve this issue, we will use functions.
To declare a function, we use the following syntax:
    def function_name():
        code
For our example, we will create a function named greet and it will look like this:
    def greet():
        print("Welcome to Coddy")
To use/call/execute the function, we write greet():
    greet()
    print("New session...")
    greet()
    print("Another session...")
    greet()
This will result in the same output as above.
Important! The function code must come before it's call
'''