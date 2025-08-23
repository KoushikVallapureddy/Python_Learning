'''
Inventory Management System:
Project Overview:
The Inventory Management System helps manage a store's inventory by adding items, updating stock, checking availability, and generating sales reports. 
It integrates dictionaries for structured data, error handling for invalid inputs, and logic operations for decision-making, making it a comprehensive and practical project.
'''

#Challenge1:
'''
Create an empty dictionary named inventory to store item details. 
Each key in this dictionary will represent an item's name, and its value will be another dictionary containing:
    price (float): The price of the item.
    stock (int): The quantity of the item in stock.

Add the following block of code at the bottom of your code:
    print(inventory)  # Should output: {}
'''

#Challenge2: Add Item
'''
Create a function named add_item that takes three arguments: item (string), price (float), and stock (int). The function should:
    Check if the item already exists in the inventory dictionary.
        If it does, print "Error: Item '<item>' already exists.".
    If the item does not exist, add it to the inventory with the provided price and stock.
        Store the price as a float and the stock as an integer.
    Print "Item '<item>' added successfully.".

Add (replace) the following block of code at the bottom of your code:
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)
'''

#Challenge3: Update Stock
'''
Create a function named update_stock that takes two arguments: item (string) and quantity (int). The function should:

    Check if the item exists in the inventory dictionary.
        If it does not exist, print "Error: Item '<item>' not found.".
    If the item exists, calculate the new stock by adding the quantity to the current stock.
        If the new stock is negative, print "Error: Insufficient stock for '<item>'." and do not update.
        Otherwise, update the stock in the inventory.
    Print "Stock for '<item>' updated successfully.".

Add (replace) the following block of code at the bottom of your code:
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)  

'''
#Challenge4: Check Availablity
'''
Create a function named check_availability that takes one argument: item (string). The function should:

    Check if the item exists in the inventory dictionary.
        If it does not exist, return "Item not found".
    If the item exists, return the current stock of the item.

Add (replace) the following block of code at the bottom of your code:
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
'''

#Challenge5: Generate Report
'''
The inventory system already has these components implemented:

    A global inventory dictionary where:
        Keys are item names (strings)
        Values are dictionaries containing:
            "price": The price of the item (float)
            "stock": Current quantity in stock (integer)
    An add_item(item, price, stock) function that adds new items to inventory
    An update_stock(item, quantity) function that updates the stock level
    A check_availability(item) function that returns the current stock level

Your task is to implement the sales_report(sales) function that:

    Takes a sales dictionary where:
        Keys are item names
        Values are quantities sold
    For each item in the sales dictionary:
        Checks if the item exists in inventory
        Checks if there's sufficient stock
        Updates the inventory by reducing stock levels
        Calculates revenue based on price and quantity sold
    Returns a formatted string with the total revenue

Handle these specific errors:

    If an item doesn't exist in inventory, print: "Error: Item '{item}' not found."
    If there's insufficient stock, print: "Error: Insufficient stock for '{item}'."

The output should be a string formatted as: “Total revenue: ${total:.2f}”


Add (replace) the following block of code at the bottom of your code:

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
'''



#Challege1 Code:
inventory = {}

#Challenge2 Code: Add item
def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")

#Test code for Challenge2 is replaced and moved to Challenge3 code. In order to test Challenge2, uncomment below code and comment other codes.
'''
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)
'''
#Challenge3 Code: Update Stock

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
        return
    new_stock = inventory[item]["stock"] + quantity
    if new_stock < 0:
        print(f"Error: Insufficient stock for '{item}'.")
        return
    inventory[item]["stock"] = new_stock
    print(f"Stock for '{item}' updated successfully.")

#Test code for Challenge3 is replaced and moved to Challenge4 code. In order to test Challenge3, uncomment below code and comment other codes.
'''
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)
'''

#Challenge4 Code: Check Availablity
def check_availability(item):
    if item in inventory:
        return inventory[item]['stock']
    else:
        return "Item not found"

#Test code for Challenge4 is replaced and moved to Challenge5 code. In order to test Challenge4, uncomment below code and comment other codes.
'''
add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
'''


#Challenge5 Code: Generate Report
def sales_report(sales):
    total_revenue = 0.0
    for item, qty in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        if inventory[item]["stock"] < qty:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= qty
        total_revenue += inventory[item]["price"] * qty
    return f"Total revenue: ${total_revenue:.2f}"

# Test code for Challenge5
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
