
#Challenge:
'''
Complete the Car class in car.py by adding a method called display_info that uses the self parameter to print the car's year, make, and model in the format:
"This car is a [year] [make] [model]".
    car.py: Contains the Car class definition where you'll add the display_info method
    driver.py: Main execution file that imports and uses the Car class
The driver.py file will import your Car class and create instances to test your implementation. Make sure your method works correctly when called from the driver file.
'''

class Car:
    def display_info(self):
        print(f"This car is a {self.year} {self.make} {self.model}")
