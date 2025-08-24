'''
Smart Contact Manager:
Create a function named organize_contacts that processes a list of contact dictionaries to create a clean contact database.
Each contact dictionary in the input list has these keys:
    name: The person's name
    email: The person's email address
    phone: The person's phone number

Your function should:
    Remove duplicate contacts (contacts with the same email or phone number)
    Standardize all emails to lowercase
    Filter out contacts with invalid email addresses
    Filter out contacts with invalid phone numbers
    Return a list of cleaned contact dictionaries

Validation rules:
    Valid email: Must contain '@' and '.', and must not have spaces
    Valid phone: Must contain exactly 10 digits (ignore non-digit characters like dashes or parentheses)

For cleaning phone numbers, you should use Python's str.isdigit() method to extract only the numeric digits from phone numbers. 
This method returns True if a character is a digit (0-9) and False otherwise, making it perfect for filtering out non-digit characters.

Example Input:
contacts = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
]

Expected Output:
[
    {"name": "John Doe", "email": "john@email.com", "phone": "1234567890"}
]

'''

def organize_contacts(contacts_list):
    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()

    for contact in contacts_list:
        name = contact.get("name", "").strip()
        email = contact.get("email", "").strip().lower()
        phone = "".join([c for c in contact.get("phone", "") if c.isdigit()])

        # Validate email
        if "@" not in email or "." not in email or " " in email:
            continue

        # Validate phone (must be exactly 10 digits)
        if len(phone) != 10:
            continue

        # Check duplicates (email or phone already seen)
        if email in seen_emails or phone in seen_phones:
            continue

        seen_emails.add(email)
        seen_phones.add(phone)

        cleaned_contacts.append({"name": name, "email": email, "phone": phone})

    return cleaned_contacts

contacts_list = [{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]
print(organize_contacts(contacts_list))