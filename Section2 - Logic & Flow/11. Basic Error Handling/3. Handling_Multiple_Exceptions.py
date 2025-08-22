'''
Handling Multiple Exceptions:
In Python, we can handle different types of exceptions in separate except blocks. 
This allows us to respond differently based on the specific error that occurs.

Start with a basic try-except structure:
    try:
        # Code that might raise exceptions
        pass
    except Exception as e:
        # Handle any exception
        pass
        
To handle multiple exceptions, add specific except blocks:
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(result)
    except ValueError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

You can also catch multiple exception types in a single except block:
    try:
        # Some code
        pass
    except (ValueError, TypeError):
        print("Invalid input type!")
The order of except blocks matters - always place more specific exceptions before more general ones.


'''