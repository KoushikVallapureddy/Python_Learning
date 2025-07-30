"""
Did you know that splitting a bill with friends can be super easy with a little bit of Python?

In this project, you'll create a simple program that calculates how much each person needs to pay, including the tip. It’s a practical way to apply what you’ve learned about variables, arithmetic operations, and basic input/output. By the end of this lesson, you’ll have a handy tool to use in real-life situations! Let’s get started!

"""
#Welcome Message
#Challenge: 
'''
Every good program starts with a welcome message, output to the screen the following string: Bill Split Calculator

'''
print('Bill Split Calculator')


#Getting Input
'''
The next part of our program is to get input from the program user.
'''

#Challenge:
'''
After the welcome message, get two numbers (float) from the user that indicate the bill amount and the tip percentage, in that order.
'''


bill_amount = float(input('Enter the bill amount: '))
tip_percentage = float(input('Enter the tip percentage: '))


#Calculating The Tip And Total
'''
Calculate the total, including the tip, print the result in the end.
'''
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
print(f'Total (including tip): ${total_amount}')


#Splitting the Bill
'''
Now we have a working program that calculates the total bill! The missing part is the splitting feature.
'''
'''
Add to the program a splitting feature:

It will take an additional number (int) from the user that indicates the number of people splitting the bill. (This will be the third input)
Calculate the amount per person by dividing the total amount by the number of people.
In the end, add another print of the amount per person.
'''

people = int(input('Enter number of people splitting among: '))
amount_per_person = total_amount / people
print(f'Each person pays: ${amount_per_person}')


#Formatted Output
'''
The last step of this project is to format the output!
For example, for the following input:
    100
    5
    2
Output in the following format:

Bill Split Calculator
Total (including tip): $105.0
Each person pays: $52.5

Note: the output should be exactly the same, so note all the uppercase letters and symbols added!
Keep in mind that when numbers are converted to float type, they will always show at least one decimal place in the output, even for whole numbers. For example, 105 will be displayed as 105.0

'''

#Changed code as per Formatted Output
