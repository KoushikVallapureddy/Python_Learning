#Challenge:
'''
You are given Python files (book.py and driver.py) to implement a book management system. In this challenge, you'll define a Book class in one file that will be imported and used in another.

Your task is to:
    Complete the Book class in book.py with an __init__ method that initializes title, author, and pages attributes
    The driver.py file will import and use your Book class to create a book object for "Harry Potter" by "J.K. Rowling" with 400 pages

Follow the detailed ToDO comments in the book.py .
'''

class Book:
 
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    
