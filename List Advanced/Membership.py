'''
Membership:
You can check whether an element is in the a list or not (in, not in):
    2 in [1, 2]      # True
    3 not in [1, 2]  # True
    3 in [1, 2]      # False
'''

#Challenege1:
'''
Create a program that receives two lists and prints a new list of all elements that are in the first list but NOT in the second list.
'''
lst1 = input().split(',')
lst2 = input().split(',')
result = []
for element in lst1:
    if element not in lst2:
        result.append(element)
print(result)
