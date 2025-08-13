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

# 4. Edit Contac
'''
The next step is to create the edit_contact function. This function will allow users to update the details of an existing contact in the Contact Book.

Your Task:

    1. Create a function named edit_contact that takes one argument: contact_book (a dictionary).
    2. Get input for the contact's name that the user wants to edit.
    3. Check if the name exists in the contact_book:
        a. If it exists, prompt the user to input new values for the contact's phone, email, and address (in that order!).
        b. If the user provides no input (presses Enter), keep the current value for that field (in this case the input will be an empty string, '').
        c. Update the contact's information in the dictionary.
        d. Print: "Contact updated successfully!".
    If the contact does not exist, print: 
        "Contact not found!".

Expected Behavior:
For a contact_book containing:
    {"Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"}}

If the user enters:
    Alice
    987-654-3210

    456 Elm St

The updated contact_book should look like this:
    {"Alice": {"phone": "987-654-3210", "email": "alice@example.com", "address": "456 Elm St"}}

If the user enters a name that does not exist:
    Bob

The output should be:
    Contact not found!

    
# 5. Delete Contact

The next step is to create the delete_contact function. This function will allow users to remove a specific contact from the Contact Book.

Your Task:
    1. Create a function named delete_contact that takes one argument: contact_book (a dictionary).
    2. Get input for the contact's name that the user wants to delete.
    3. Check if the name exists in the contact_book:
        a. If it exists, remove the contact from the dictionary.
        b. Print: "Contact deleted successfully!".
    4. If the contact does not exist, print: "Contact not found!".

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
    

# 4. Edit Contact

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()
        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print('Contact updated successfully!')
    else:
        print('Contact not found!')

edit_contact(contact_book)

# 5. Delete Contact
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print('Contact deleted successfully!')
    else:
        print('Contact not found!')

delete_contact(contact_book)

    







