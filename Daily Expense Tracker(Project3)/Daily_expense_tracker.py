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

#Code:
while True:
    choice = input()
    if choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
'''

#Challenge3:
'''
Add Expense:

Handle the option where the user adds an expense (1).
1. Initialize in the start of the program an empty expenses list
2. When the user selects 1 as a choice, get another input from the user, a float, and add its value to the expenses list.
3. After adding, output:
    Expense added successfully!

#Code:
expenses = []
while True:
    choice = input()
    if choice == '1':
        expenses.append(float(input()))
        print('Expense added successfully!')
    elif choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
'''

#Challenge4: Veiw All Expenses
'''
View All Expenses:

Handle the option to view all the expenses (2).
If the expenses list is empty, output:
    No expenses recorded yet.

Otherwise, output the list in the following format:
    Your expenses:
    1. 23.1
    2. 35.5
    3. 99.99
    4. 15.2
Assuming the expenses entered before were 23.1, 35.5, 99.99 and 15.2. (In that order!)


#Code:
expenses = []
while True:
    choice = input()
    if choice == '1':
        expenses.append(float(input()))
        print('Expense added successfully!')
    elif choice == '2':
        if not expenses:
            print('No expenses recorded yet.')
        else:
            print('Your expenses:')
            for i in range(len(expenses)):
                print(f'{i + 1}. {expenses[i]}')
    elif choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
'''

expenses = []
while True:
    choice = input()
    if choice == '1':
        expenses.append(float(input()))
        print('Expense added successfully!')
    elif choice == '2':
        if not expenses:
            print('No expenses recorded yet.')
        else:
            print('Your expenses:')
            for i in range(len(expenses)):
                print(f'{i + 1}. {expenses[i]}')
    elif choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break



    
