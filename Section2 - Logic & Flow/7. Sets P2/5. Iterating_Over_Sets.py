'''
Iterating over sets:
Iterating over a set is similar to iterating over a list or a dictionary. You can use a for loop to go through each element in a set. However, it's important to remember that sets are unordered, so the elements will not be processed in a specific sequence.

Here's an example of iterating over a set:
    my_set = {1, 2, 3, 4, 5}
    for element in my_set:
        print(element)

Output:
    1
    2
    3
    4
    5

In this example, the for loop iterates over each element in my_set and prints it. 
The order of the elements in the output may vary because sets do not maintain a specific order.

If you need to access the elements of a set in a specific order, you can convert the set to a list and then iterate over the sorted list:
    my_set = {5, 2, 8, 1, 3}
    sorted_list = sorted(list(my_set))
    for element in sorted_list:
        print(element)

Output:
    1
    2
    3
    5
    8

In this example, we first convert my_set to a list using list(my_set), then sort the list using sorted(). 
The for loop then iterates over the sorted list, printing each element in ascending order.

'''

#Challenge1:
'''
Create a function named iterate_and_filter_set that takes a set input_set as an argument. 
The function should iterate over the elements in the set and filter out numbers that are greater than 10. 
The function should return a new set containing only the numbers that are less than or equal to 10.

'''
def iterate_and_filter_set(input_set):
    filtered_set = set()
    for element in input_set:
        if element <= 10:
            filtered_set.add(element)
    return filtered_set

input_set = {10}
print(iterate_and_filter_set(input_set))


#Challenge2:
'''
Create a function named filter_and_square_set that takes a set input_set as an argument. 
The function should iterate over the elements in the set, filter out even numbers, and square the remaining odd numbers. 
The function should return a new set containing only the squared values of the odd numbers from the input set.

For example, if the input set is {1, 2, 3, 4, 5}, the function should return {1, 9, 25}.
'''
def filter_and_square_set(input_set):
    filtered_set = set()
    for element in input_set:
        if element %2 == 1:
            element = element * element
            filtered_set.add(element)
    return filtered_set

input_set = {21,22,23,24,25}
print(filter_and_square_set(input_set))

