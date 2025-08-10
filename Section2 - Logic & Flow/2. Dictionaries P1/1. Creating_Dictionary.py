'''
Dictionary:

A dictionary in Python is a collection of data that stores data in key-value pairs. 
Unlike lists, which use indices to access elements, dictionaries use keys. Each key in a dictionary must be unique, and it is associated with a value.

Think of a real-world dictionary. You look up a word (the key) to find its meaning (the value). 
In Python, a dictionary works similarly. For example, you can have a dictionary where the keys are names of countries and the values are their capitals.

Dictionaries are useful when you have data that is naturally paired together and when you need to quickly access a value by knowing its associated key.
'''

'''
Creating a Dictionary:
To create a dictionary in Python, you use curly braces {} and specify the key-value pairs within them. 
Each key-value pair is written as key: value, and multiple pairs are separated by commas.

Here's how you can create a dictionary:

# Creating a dictionary of country capitals
    country_capitals = {
        "USA": "Washington, D.C.",
        "France": "Paris",
        "Japan": "Tokyo"
    }

# Creating a dictionary of employee information
    employee = {
        "name": "John Doe",
        "age": 30,
        "position": "Software Engineer"
    }

# Creating an empty dictionary
    empty_dict = {}

    
In the first example, country_capitals is a dictionary with country names as keys and their capitals as values. 
In the second example, employee is a dictionary containing information about an employee. 
The third example shows how to create an empty dictionary, which can be useful when you want to add items to it later.

'''

#Challenge:
'''
Create a function named create_student_dict that takes three parameters: name, age, and major. 
The function should return a dictionary where the keys are "name", "age", and "major", and the values are the corresponding values passed to the function.

For example, calling create_student_dict("Alice", 20, "Computer Science") should return a dictionary with the following key-value pairs:
    Key: "name", Value: "Alice"
    Key: "age", Value: 20
    Key: "major", Value: "Computer Science"
'''

def create_student_dict(name, age, major):
    student_dict = {
        'name' : name,
        'age' : age,
        'major' : major
    }
    return student_dict
name = input("Enter name: ")
age = int(input('Enter age: '))
major = input('Enter major: ')
print(create_student_dict(name, age, major))
