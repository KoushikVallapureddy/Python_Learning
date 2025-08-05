'''
The Enumerate Function:

The enumerate() function allows you to loop through a sequence (like a list, tuple, or string) while keeping track of the index position of each item.

without enumerate() we would access both the index and the value the following way:
    fruits = ["apple", "banana", "orange"]
    for i in range(len(fruits)):
        print(f"Index {i}: {fruits[i]}")
enumerate() is a more elegant way to get both index and value:
    fruits = ["apple", "banana", "orange"]
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
Both examples will output:

Index 0: apple
Index 1: banana
Index 2: orange
'''

#Challenge1:
'''
Write a program that receives a list of numbers as input (given), and prints a list of the indices of the numbers that are either below 50 or they are divisible by 5. 

lst = list(map(int, input().split(",")))
result = []
for index, num in enumerate(lst):
    if num < 50 or num % 5 == 0:
        result.append(index)
print(result)

'''

#Challenge2:
'''
Write a program that receives a list of words as input (given), and prints a list of the indices of the words that are either longer than 3 characters or start with the letter 'a' (case-sensitive).

To check if a string starts with some substring use: str.startswith("substring")
'''

lst = input().split()
result = []
for index, word in enumerate(lst):
    if len(word.strip()) > 3 or word.startswith('a'):
        result.append(index)
print(result)




