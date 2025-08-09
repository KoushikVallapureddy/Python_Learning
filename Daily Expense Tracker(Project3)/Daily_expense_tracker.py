'''
Project Overview:
You will build a simple program to manage daily expenses.
The user can add, view, and clear expenses, as well as calculate the total and average.
This project reinforces basic programming concepts like lists, loops, and functions in a practical, real-life scenario.
'''

#Challenge1:
'''
As always, output a welcome message to the program:
    print("Welcome to the Daily Expense Tracker!")

After this, add a new line and output the menu:
    Menu:
    1. Add a new expense
    2. View all expenses
    3. Calculate total and average expense
    4. Clear all expenses
    5. Exit
'''

print('Welcome to the Daily Expense Tracker!\n')
print('Menu:')
print('1. Add a new expense')
print('2. View all expenses')
print('3. Calculate total and average expense')
print('4. Clear all expenses')
print('5. Exit')

#Challenge2:
'''
Now let's create the actual program!
1. Create an infinite while loop (refer the hint if not sure how to do so)
2. In each iteration of the loop, get input from the user, this will be the choice (1 - 5 from the menu)
3. Handle the first case, if the choice is equal to 5, exit the program (loop) and output:
    Exiting the Daily Expense Tracker. Goodbye!
'''

while True:
    choice = input('Enter your choice (1-5): ')
    if choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
