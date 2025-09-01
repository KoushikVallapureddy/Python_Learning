#Challenge:
'''
In this challenge, you'll implement a class hierarchy.

You'll need to edit these files:
    device.py: Implement the base Device class
    screen.py: Implement Screen class that inherits from Device
    computer.py: Implement Computer class that inherits from Device
    laptop.py: Implement Laptop class with multiple inheritance
    driver.py - Implement test cases that will verify your implementation works correctly
Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
'''

class Device:
    # TODO: Implement the power_on method
    # TODO: This method should return the string "Device powered on"
    def power_on(self):
        return 'Device powered on'