'''
Recap-Shopping Cart Errors:

Create a program that simulates a shopping cart with error handling. Your task is to:
    1. Create a function called handle_shopping_cart that processes customer orders
    2. The function should accept a list of order strings in the format "item:quantity"
    3. Process each order by:
        a. Splitting the input string to get the item and quantity
        b. Converting the quantity to an integer
        c. Adding the item to a shopping cart dictionary with the quantity as value
        d. If an item already exists in the cart, update its quantity
    4. Handle these specific errors:
        a. If the input format is incorrect (missing colon), print "Invalid format: {order}"
        b .If the quantity is not a valid number, print "Invalid quantity: {order}"
        c. If the quantity is negative, print "Negative quantity not allowed: {order}"
    5. Return the completed shopping cart dictionary
'''

def handle_shopping_cart(orders):

    shopping_cart = {}
    for order in orders:
        try:
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
            item, quantity_str = order.split(":")
            try:
                quantity = int(quantity_str)
            except ValueError:
                print(f"Invalid quantity: {order}")
                continue
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue
            shopping_cart[item] = shopping_cart.get(item, 0) + quantity
        except Exception as e:
            print(f"Unexpected error processing order '{order}': {e}")
    return shopping_cart
            
orders = eval(input())
print(handle_shopping_cart(orders))