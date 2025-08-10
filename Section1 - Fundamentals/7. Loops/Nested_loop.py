'''
A nested loop is a loop inside another loop. 
The inner loop completes all its iterations for each iteration of the outer loop.
Let's create a simple nested loop:
# Outer loop
for i in range(3):
    print(f"Outer loop iteration: {i}")
    
    # Inner loop
    for j in range(2):
        print(f"  Inner loop iteration: {j}")
When you run this code, you'll see:
Outer loop iteration: 0
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 1
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 2
  Inner loop iteration: 0
  Inner loop iteration: 1

Notice that for each iteration of outer loop, inner loop completes all of it's iterations.
'''

#Challenge1:
'''
Write a function named print_pattern that prints a rectangle pattern of stars (*).
The function should:
Take two parameters: rows and cols (both integers)
Use nested loops to print a rectangle with the given dimensions
Each row should contain cols stars
The pattern should have rows rows in total
Example output for print_pattern(3, 4):

def print_pattern(rows, cols):
    # Outer loop for rows
    for i in range(rows):
        # Inner loop for columns
        row_string = ""
        for j in range(cols):
            row_string += '*'
        # Move to the next line after printing a row
        print(row_string)

# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)


'''


#Challenge2:

'''
Write a program that finds all pairs of numbers that multiply to give n using numbers from 1 to n.
The program should show all possible combinations, including duplicate pairs in reverse order. 
For example, both "1 6" and "6 1" should be shown, as they are considered different arrangements of the same pair.
 Numbers can also be paired with themselves if their product equals n.

For example if n = 12, the output should be:
1 12
2 6
3 4
4 3
6 2
12 1

Because:
1 * 12 = 12
2 * 6 = 12
3 * 4 = 12
4 * 3 = 12
6 * 2 = 12
12 * 1 = 12
'''

n = int(input('Enter the number:'))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(f'{i} {j}')