'''
As of now we learned how to print simple strings, but sometimes we need to insert variable values into string.
for example: 
age =10
print("His age is: age")
This will print: His age is: age instead of His age is: 10
To make this work, we will use f-strings:
age =10
print(f'His age is: {age}')
This prints His age is: 10
Before the quotation marks "" we add the letter f and inside the string, wherever we put curly braces {} it will insert the value of what is written inside it.
'''

#Challenge:
'''
You are given a code that stores a random string as input to a variable named rnd.

Print to the console "The input is: " and the random string that is inside the variable rnd.
'''

rnd = input()
print('The input is:', rnd)


