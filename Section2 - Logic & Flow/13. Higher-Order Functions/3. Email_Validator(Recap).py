'''
Recap- Email Validator
Create a function named clean_email_list that takes a list of email addresses and returns a list of valid, standardized email addresses.
Requirements:
    - Convert all emails to lowercase and strip all whitespace at the beginning or end
    - Only keep emails that:
        - Contain exactly one '@' symbol
        - Have at least one character before the '@'
        - Have at least one character after the ‘@’

Use map() and filter() to solve the problem.
'''

def clean_email_list(emails):
    cleaned = map(lambda e: e.strip().lower(), emails)
    valid_emails = filter(lambda e: e.count("@") == 1 and e.index("@") > 0 and e.index("@") < len(e) - 1, cleaned)
    return list(valid_emails)

emails = input().split(', ')
print(clean_email_list(emails))