'''
Looping Through Dictionaries:
Looping through a dictionary allows you to access each key-value pair and perform operations on them. 
Python provides several ways to iterate through dictionaries, making it easy to work with their contents.
Looping thrrough keys:
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    for key in my_dict:
        print(key)
Output:
    name
    age
    city    

Looping through values:
    for value in my_dict.values():
        print(value)
Output:
    Alice
    30
    New York

Looping through key-value pairs:
    for key, value in my_dict.items():
        print(f'{key}: {value}')
Output:
    name: Alice
    age: 30
    city: New York
    
In these examples, the first loop iterates over the keys of the dictionary. 
The second loop iterates over the values using the values() method. 
The third loop uses the items() method to iterate over both keys and values simultaneously.
'''

#Challenge1:
'''
Create a function named print_employee_details that takes a dictionary employee_data as an argument. 
The function should loop through the dictionary and print each key-value pair in the format 'key: value'. 
If the dictionary is empty, the function should print 'No data available'.

def print_employee_details(employee_data):
    if not employee_data:
        print('No data available')
    else:
        for key, Value in employee_data.items():
            print(f'{key}: {Value}')

employee_details = {'Alice': 'Engineer', 'Bob': 'Manager', 'Charlie': 'Analyst'}
print_employee_details(employee_details)

'''

#Challenge2:
"""
Create a function named print_product_details that takes a dictionary product_data as an argument. 
The function should loop through the dictionary and print each key-value pair in the format 'Key: Value', with the key capitalized. 
If the dictionary is empty, the function should print 'No product information available'.
"""

def print_product_details(product_data):
    if not product_data:
        print('No product information available')
    else:
        for key, value in product_data.items():
            print(f'{key.capitalize()}: {value}')
            
product_details = {"name":"Headphones","brand":"Sony","price":199.99,"stock":30}
print_product_details(product_details)

