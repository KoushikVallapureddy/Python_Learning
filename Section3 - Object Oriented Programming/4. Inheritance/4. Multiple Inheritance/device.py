'''
In this challenge, you'll implement a multi-file class system demonstrating multiple inheritance with smartphones. Each class is organized in its own file for better code organization.

You'll need to edit these files:
    device.py - Implement the Device base class
    internet.py - Implement the Internet base class
    smartphone.py - Implement the Smartphone class that inherits from both base classes
    driver.py - Implement test cases that will verify your implementation works correctly

Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
'''

class Device:
    def __init__(self, brand):
        # TODO: Store the brand parameter as an instance attribute (self.brand)
        self.brand = brand
        

    
    def power_on(self):
        # TODO: Return the string "Device powered on"
        return 'Device powered on'
        