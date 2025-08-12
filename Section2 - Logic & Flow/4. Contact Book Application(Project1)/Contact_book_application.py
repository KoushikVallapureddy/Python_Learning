#1. Display Menu
'''
#Display Menu:
In this project, we will build a Contact Book application step by step by breaking it into small, manageable functions. 
The first step is to create a display_menu function.

Create a function named display_menu that prints the main menu options for the Contact Book.

The menu should include the following options:
    Add Contact
    View Contact
    Edit Contact
    Delete Contact
    List All Contacts
    Exit
This function will be the starting point of the program, helping users navigate through the options.
Check the test case for the output format!

'''

# 2. Add Contact
'''
Now, create the add_contact function that takes one argument: contact_book (a dictionary). The function should:
    Get input for the contact's name, phone, email, and address.
    Check if the name already exists in the dictionary. If it does, print: "Contact already exists!".
    If not, save the contact in the following format:

        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
Then print: "Contact added successfully!".
'''

# 3. View Contact
'''
Create a function named view_contact that displays details of a specific contact.

Your function should:
    Take a contact book dictionary as input
    Ask the user to enter a contact name
    Display the contact's details if found
    Print "Contact not found!" if the contact doesn't exist

When displaying a contact, use this exact format:
    Name: [name]
    Phone: [phone]
    Email: [email]
    Address: [address]

Example:
If the contact book contains Alice's information and the user enters "Alice", output:
    Name: Alice
    Phone: 123-456-7890
    Email: alice@example.com
    Address: 123 Main St

If the user enters "Bob" (who doesn't exist), output:
    Contact not found!

'''

# 1. Display name: 

def display_menu():
    print('Contact Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Edit Contact')
    print('4. Delete Contact')
    print('5. List All Contacts')
    print('6. Exit')
display_menu()

# 2. Add Contact:

def add_contact(contact_book):
    name = input()
    if name in contact_book:
        print('Contact already exists!')
        return
    phone = input()
    email = input()
    address = input()
    contact_book[name]= {
        "phone" : phone,
        "email" : email,
        'address' : address}
    print('Contact added successfully!')

contact_book = {}
add_contact(contact_book)



#3. View Contact
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print(f'Name: {name}')
        print(f'Phone: {contact["phone"]}')
        print(f'Email: {contact["email"]}')
        print(f'Address: {contact["address"]}')
    else:
        print('Contact not found!')

view_contact(contact_book)
    





