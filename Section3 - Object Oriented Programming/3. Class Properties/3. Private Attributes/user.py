#Challenge:
'''
Complete the User class in user.py with private password functionality, then use it in driver.py. Follow the TODO comments to implement password checking and changing methods.
'''
class User:
    def __init__(self, password):
        # TODO: Store the password as a private attribute using double underscore (__)
        #       This makes it harder to access from outside the class
        self.__password = password
    
    def check_password(self, input_password):
        # TODO: Return True if input_password matches the stored private password
        #       Return False otherwise
        return input_password == self.__password
    
    def change_password(self, old_password, new_password):
        # TODO: Check if old_password is correct using the check_password method
        # TODO: If old_password is correct, update the private password to new_password and return True
        # TODO: If old_password is incorrect, return False without changing the password
        if self.check_password(old_password):
            self.__password = new_password
            return True
        return False