from temperature import Temperature

# Test the class:
temp = Temperature(25)

print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

temp.fahrenheit = 98.6

print(f"{temp.celsius}°C is {temp.fahrenheit}°F")

# TODO: Uncomment the line below to test invalid temperature handling
# temp.celsius = -300
