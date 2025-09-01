from device import Device
from screen import Screen
from computer import Computer
from laptop import Laptop

def explain_mro(class_name):
    print(f"MRO for {class_name.__name__}:")
    for cls in class_name.__mro__:
        print(cls.__name__)
    
    instance = class_name()
    result = instance.power_on()
    print(f"Power on result: {result}")
    print()  # Empty line for better readability
    
# Test your code
explain_mro(Device)
explain_mro(Screen)
explain_mro(Computer)
explain_mro(Laptop)