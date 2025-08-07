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

#Challenge1:
'''

Create a program that receives a list as input (given) and prints the following sliced list (depends on the list length):
    For odd-length lists: take the middle item and one item on each side (3 items total)
    For even-length lists: take the two middle items
When dividing numbers:
    / gives you a decimal number (5/2 = 2.5)
    // removes the decimal part (5//2 = 2)
For this challenge, use // because list slicing only works with whole numbers.


lst = input().split(',')
length = len(lst)
mid = length // 2
if length % 2 == 0:
    result = lst[mid-1:mid+1]
else:
    result = lst[mid-1:mid+2]
print(result)

'''

