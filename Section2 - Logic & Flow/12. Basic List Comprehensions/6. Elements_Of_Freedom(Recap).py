'''
Create a function named elements_of_freedom that processes a list of string elements according to specific rules.

Your function should:

    Filter out elements that have fewer than 5 characters
    Convert the remaining elements to uppercase
    Remove any duplicate elements
    Return a list of the unique uppercase elements

Use list operations to efficiently process the data.

Example:
Input: ["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]
Output: ['APPLE', 'BANANA', 'CHERRY', 'GRAPE']
'''

def elements_of_freedom(elements):
    filtered_list = [word for word in elements if len(word) >= 5]
    uppercase = [word.upper() for word in filtered_list]
    unique_elements = list(dict.fromkeys(uppercase))
    return unique_elements

elements = eval(input())
print(elements_of_freedom(elements))