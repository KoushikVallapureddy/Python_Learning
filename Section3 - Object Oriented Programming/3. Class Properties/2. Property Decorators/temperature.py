#Challenge:
'''
Complete the Temperature class in temperature.py that converts between Celsius and Fahrenheit. Then use this class in driver.py to test temperature conversions. Follow the TODO comments in both files for step-by-step instructions.
'''
class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
