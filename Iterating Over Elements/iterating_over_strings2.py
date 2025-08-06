'''
Iterating over strings Part 2:

String splitting allows you to break a string into a list, while joining lets you combine list items into a string.
The split() method divides a string into a list of substrings based on a delimiter.

Split by whitespace:
    text = "apple banana cherry"
    fruits = text.split()
    print(fruits)
# ['apple', 'banana', 'cherry']

Split with specific delimiter:
    data = "john,25,new york"
    data = data.split(',')
    print(data)
# ['john', '25', 'new york']

The join() method combines elements of an iterable into a single string.

Basic joining:
    words = ['Hello', 'World', 'Python']
    text = ' '.join(words)
    print(text)
# "Hello World Python"

Join with different separator:
    fruits = ['apple', 'banana', 'cherry']
    line = ','.join(fruits)
    print(line)
# "apple,banana,cherry"

'''

#Challenge1:
'''
Write a program that takes two inputs: a text string and a delimiter character. 
The program should split the text by whitespace into words, 
then join these words using the specified delimited character and print the resulting string.


text = input()
delimiter = input()
result = text.split()
result = delimiter.join(result)
print(result)

'''

#Challenge2:
'''
Create a program that takes two inputs: a string of numbers separated by spaces, and a prefix string. 
The program should split the number string into individual numbers, 
add the prefix to each number, then join these modified numbers back into a single string separated by spaces. 
Finally, print the resulting string.
'''

numbers = input()
prefix = input()

result = numbers.split()
result = [prefix + num for num in result]
result = ''.join(result)
print(result)   


