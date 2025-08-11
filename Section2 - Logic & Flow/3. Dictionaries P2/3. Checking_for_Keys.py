'''
Chekcing for keys:
When working with dictionaries, you often need to check if a specific key exists. 
Python provides simple ways to check for the presence of keys in a dictionary.

Using the in keyword:
    my_dict = {'name': 'Alice', 'age': 30}

    # Check if 'name' is a key in the dictionary
    if 'name' in my_dict:
        print('Name exists in the dictionary')

    # Check if 'city' is a key in the dictionary
    if 'city' not in my_dict:
        print('City does not exist in the dictionary')

In this example, we use the in keyword to check if 'name' is one of the keys in my_dict. 
We also use not in to check if 'city' is not a key in the dictionary.

Using the keys() method:
    my_dict = {'name': 'Alice', 'age': 30}

    # Check if 'age' is in the list of keys
    if 'age' in my_dict.keys():
        print('Age exists in the dictionary')

Here, my_dict.keys() returns a list of all keys in the dictionary, and we use in to check if 'age' is in that list.
'''

#Challenge1:
'''
You are managing a dictionary of employee data, where each key is an employee's name and the value is their department. Your task is to:

Check if "Alice" is a key in the dictionary.
    If it exists, print: "Alice is in the company."
Check if "John" is not a key in the dictionary.
    If it does not exist, print: 
    "John is not in the company."
'''

employee_data = {'Alice':'HR', 'Bob':'Engineering', 'Diana':'Marketing'}
# Check if "Alice" is a key in the dictionary
if 'Alice' in employee_data:
    print('Alice is in the company.')
#Check if "John" is not a key in the dictionary
if 'John' not in employee_data:
    print('John is not in the company.')

