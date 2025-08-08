'''
List Slicing Part2:

Slicing has another step parameter: lst[start:stop:step], For example consider this list:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Gets every second element from index 1 to 8:
    print(numbers[1:8:2])
    # Output: [1, 3, 5, 7]

Gets every third element from index 2:
    print(numbers[2::3])
    # Output: [2, 5, 8]

Slicing also supports negative indices.
Counting from end:
    print(numbers[-3:])
    # Output: [7, 8, 9]
Here, -3 means "start 3 positions from the end"

Count until end:
    print(numbers[:-2])    
    # Output: [0, 1, 2, 3, 4, 5, 6, 7]
Here, -2 means "stop 2 positions from the end" (exclusive)

Reversing with negative step:
    print(numbers[::-1])
    # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Empty space before first : means “start from beginning”
Empty space between : means “go until the end”
-1 means "move backwards one step at a time" 

'''
#Challenge1:
'''
Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:
    A list containing every third element, starting from index 1 (the second element)
    A list containing all the elements from the 6th element to the 1st in reverse order
    A list containing every second element starting from the middle of the list to the end

lst = input().split(',')
length = len(lst)
result1 = lst[1::3]
result2 = lst[5::-1]
mid = length//2
result3 = lst[mid::2]
print(result1)
print(result2)
print(result3)

'''

#Challenge2:
'''
Create a program that receives a list as input and prints four new lists based on the following slicing operations:

    A list containing every fourth element, starting from index 2
    A list containing all elements from the 3rd element to the 3rd to last element
    A list containing every element in reverse order, skipping every other element
    A list containing the first three and last three elements of the original list
Name the lists list1, list2, list3 and list4 - accordingly.
'''

orginal_list = input().split(',')
length = len(orginal_list)
list1 = orginal_list[2::4]
list2 = orginal_list[2:-2]
list3 = orginal_list[length::-2]
list4 = orginal_list[:3] + orginal_list [-3:]
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)

