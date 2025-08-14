'''
Basic Operations:
Sets come with built-in operations that allow you to perform common set-related tasks efficiently. These operations include adding elements, removing elements, and checking for the presence of elements.

Adding an element to a set:
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)
    # Output: {1, 2, 3, 4}

Removing an element from a set: (raises an error if it does not exist!)
    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)
    # Output: {1, 3}

Checking for the presence of an element:    
    my_set = {1, 2, 3}
    print(2 in my_set)
    # Output: True
    print(4 in my_set)
    # Output: False
'''

#Challenge:
'''
Create a function named manage_set that takes three arguments: set1 (a set), element_to_add, and element_to_remove. The function should perform the following operations:

1. Add element_to_add to set1.
2. Attempt to remove element_to_remove from set1. If the element is not in the set, do nothing.
3. Check if the number 5 is in set1. If it is, return the string "5 is in the set". Otherwise, return the string "5 is not in the set".


def manage_set(set1, element_to_add, element_to_remove):
    set1.add(element_to_add)
    if element_to_remove in set1:
        set1.remove(element_to_remove)
    if 5 in set1:
        print("5 is in the set")
    else:
        print("5 is not in the set")

set1 = input()
element_to_add = 3
element_to_remove = 4
manage_set(set1, element_to_add, element_to_remove)

'''

#Challenge2:
'''
Create a function named manage_list that takes three arguments: list1 (a list of integers), element_to_append, and index_to_remove. The function should perform the following operations:

1. Append element_to_append to the end of list1.
2. Attempt to remove the element at index index_to_remove from list1. If the index is out of range, do nothing.
3. Check if list1 has more than 3 elements. If it does, return the string "The list has more than 3 elements". 
    Otherwise, return the string "The list has 3 or fewer elements".
'''


def manage_list(list1, element_to_append, index_to_remove):
    list1.append(element_to_append)
    if 0 <= index_to_remove < len(list1):
        list1.pop(index_to_remove)
    return "The list has more than 3 elements" if len(list1) > 3 else "The list has 3 or fewer elements"

list1 = list(input().split())
element_to_append = int(input())
index_to_remove = int(input())
print(manage_list(list1, element_to_append, index_to_remove))
