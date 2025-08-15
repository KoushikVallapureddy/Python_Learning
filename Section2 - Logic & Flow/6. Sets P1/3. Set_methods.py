'''
Set Methods:
Here are even more essential set methods:
discard(element): Removes the specified element from the set if it exists. Does not raise an error if the element is not found.
    my_set = {1, 2, 3}
    my_set.discard(3)    # Removes 3 from the set
    my_set.discard(4)    # No error, even though 4 is not in the set
    print(my_set)
    # Output: {1, 2}

pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
    my_set = {1, 2, 3}
    element = my_set.pop()  # Removes and returns an arbitrary element
    print(element)
    # Output: 1 (or another element, as it's arbitrary)
    print(my_set)
    # Output: {2, 3} (or a different set, depending on the popped element)

clear(): Removes all elements from the set, making it empty.
    my_set = {1, 2, 3}
    my_set.clear()       # Removes all elements
    print(my_set)
    # Output: set()
'''

#Challenge:
'''
Write a program that performs the following tasks:

1. Create a set called numbers containing the values 10, 20, 30, 40, 50.
2. Use the discard() method to remove 35 from the set.
3. Use the pop() method to remove an arbitrary element and store it in a variable called popped_element.
4. Use the clear() method to empty the set.
5. Print the following:
    The set after using discard().
    The value of popped_element.
    The set after using clear().
'''

numbers = {10, 20, 30, 40, 50}
numbers.discard(35)
print(numbers)
popped_element = numbers.pop()
print(popped_element)
numbers.clear()
print(numbers)

