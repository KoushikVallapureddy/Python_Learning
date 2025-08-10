'''
Round Numbers:
The round() function rounds numbers to the nearest value.
    round(number, ndigits)

    a. number: The value to round.
    b. ndigits: Decimal places to keep (optional).

Examples:
    print(round(4.567))     # 5
    print(round(4.567, 2))  # 4.57
    print(round(456.78, -1))  # 460

Python rounds halfway cases to the nearest even number:
    print(round(2.5))  # 2
    print(round(3.5))  # 4
'''

#Challenge1:
'''
Write a program that:
    Takes a number as input from the user (float).
    Takes the number of decimal places to round to (integer).
    Outputs the rounded number.


number = float(input())
integer = int(input())
rounded_number = round(number, integer)
print(rounded_number)

'''

#Challenge2:
'''
Create a function named calculate_discount that takes two parameters:
    price: The original price of an item (float)
    discount_percentage: The discount percentage (float)

The function should:
    Calculate the discount amount
    Subtract the discount amount from the original price
    Round the result to 2 decimal places
    Return the final discounted price

For example, if the original price is $100 and the discount is 20%, the function should return $80.00.
'''

def calculate_discount(price, discount_percentage):
    discount_amount = price * discount_percentage /100
    final_amount = price - discount_amount
    final_discounted_price = round(final_amount, 2)
    return final_discounted_price

price = float(input())
discount_percentage = float(input())
calculate_discount(price, discount_percentage)
print(calculate_discount(price, discount_percentage))




