'''
Recap- House of Lists:

Create a function named house_of_lists that takes a list of lists list_of_lists as an argument. 
Each inner list contains numbers. The function should use list comprehensions to perform the following operations:
    Filter out inner lists that have a sum greater than 50.
    From the remaining inner lists, extract numbers that are less than 5.
    Combine all extracted numbers into a single list.
    Return the combined list of numbers.
'''

def house_of_lists(list_of_lists):
    filtered_lists = [inner for inner in list_of_lists if sum(inner) <= 50]
    combined = [num for inner in filtered_lists for num in inner if num < 5]
    return combined

list_of_lists = eval(input())
print(house_of_lists(list_of_lists))