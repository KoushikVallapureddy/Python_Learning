'''
The continue statement stops the current iteration and continues to the next iteration. 
For example:
for i in range(3, 9):
    if i == 5:
        continue
    print(i)
The loop will iterate through the numbers from 3 to 8, and when it reaches i=5 it will skip that iteration and continue to the next one. The output is:
3
4
6
7
8
'''

#Challenge1:
'''
You are given a code which prints the numbers from 1 to 20 (including).
Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...).


for i in range(1,21):
    if i % 2 == 1:
        continue
    print(i)

'''

#Challenge2:
'''
You are given a code which prints the numbers from 1 to 100 (including).
Your task is to add if and continue statements so that all numbers except multiples of 3 will be printed. In other words, skip printing any number that is divisible by 3.
For example, the output should include 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, and so on, but should skip 3, 6, 9, 12, 15, 18, etc.
'''

for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i)