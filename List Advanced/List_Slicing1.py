'''
List Slicing Part1:
Slicing allows us to extract portions of a list using the following syntax: lst[start:stop]. 
For example consider this list:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Getting a portion of the list:
    print(numbers[2:6])
    # Output: [2, 3, 4, 5]
This gets elements from index 2 (inclusive) to index 6 (exclusive)
Omitting start parameter:
    print(numbers[:5])
    # Output: [0, 1, 2, 3, 4]
When start is omitted, slice begins from index 0
Omitting stop parameter:
    print(numbers[5:])
    # Output: [5, 6, 7, 8, 9]
When stop is omitted, slice goes until the end
'''

