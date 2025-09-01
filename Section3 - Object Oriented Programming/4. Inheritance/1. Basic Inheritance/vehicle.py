#Challenge:
'''
Create:
    vehicle.py: Contains the parent Vehicle class
    car.py: Contains the Car class that inherits from Vehicle
    driver.py: Main file to test your implementation

Each file contains detailed TODO comments to guide you through the implementation. You'll need to:
    Complete the Vehicle class with make and model attributes
    Implement proper class inheritance in the Car class
    Set up the correct import statements between files
    Create and test objects in the driver file

Follow the TODO comments carefully as they provide step-by-step guidance to the solution.
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f'Vehicle: {self.make} {self.model}')
        