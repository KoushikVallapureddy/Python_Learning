#Challenge:
'''
In this challenge, you'll implement a Person and Employee class hierarchy using inheritance.
    person.py: Contains the Person class with name and age attributes
    employee.py: Contains the Employee class that inherits from Person
    driver.py: Main file to test your implementation
Each file contains detailed TODO comments to guide you through the implementation.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

