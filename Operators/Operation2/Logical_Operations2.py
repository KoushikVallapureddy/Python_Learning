"""
In Python, you can combine multiple conditions using logical operators(and, or, not) to create more complex expressions.
lets create a condition that checks if a number is both positive and even:
number = 4
Now lets check if number is posiitive:
is_positive = number > 0
Let's check if number is even:
is_even = number % 2 == 0
We can combime these two conditions using the 'and' operator: 
result = is_positive and is_even
This evaluates to True because 4 is both positive and even.
for more direct approach, we can write:
result = number > 0 and number % 2 == 0
This will also evaluate to True.

Similarly, we can use the 'or' operator to check if a number is either negative or odd:
number = -2
is_negative = number < 0
is_odd = number % 2 != 0
result = is_negative or is_odd
This evaluates to True because -2 is negative, even though it is not odd.

"""

#Challenge1:
'''
Write code that checks if a person is eligible to drive. A person is eligible to drive if ALL of the following conditions are met:

The person is at least 18 years old
The person has a license
The person has insurance
'''
"""
age = int(input("Enter your age: "))
has_license =int(input('Do you have license? (1 for true and 0 for false): '))
has_insurance = int(input('Do you have insurance? (1 for true and 0 for false):'))
is_eligible_to_drive = age>=18 and has_license and has_insurance
print('Is the person eligible to drive?', is_eligible_to_drive)



age = int(input("Enter your age: "))
has_license =input().lower == 'yes'
has_insurance = input().lower() == 'yes'
is_eligible_to_drive = age>=18 and has_license and has_insurance
print('Is the person eligible to drive?', is_eligible_to_drive)


"""
#Challenge 2:
'''
You're helping a weather app determine suitable outdoor activities based on weather conditions. Create a program that uses logical operations to determine if certain activities are possible.

Initialize the following variables:

is_sunny with the value True
temperature with the value 25
wind_speed with the value 10
water_temperature with the value 22
Write the following logical expressions to determine if:

can_go_hiking: It's sunny AND temperature is above 15°C AND wind speed is below 20 km/h
can_go_swimming: It's sunny AND temperature is above 20°C AND water temperature is above 18°C
cannot_go_outside: It's NOT sunny OR temperature is below 10°C OR wind speed is above 30 km/h

'''
'''
is_sunny = input('is it sunny? (yes or no): ').lower() == 'yes'
Temperature = int(input('Enter the temperature in C: '))
Wind_speed = int(input('Enter the wind speed in km/hr: '))
Water_Temperature = int(input('Enter the water temperature in C: '))

can_go_hiking = is_sunny and Temperature > 15 and Wind_speed < 20
can_go_swimming = is_sunny and Temperature > 20 and Water_Temperature > 18
cannot_go_outside = not is_sunny or Temperature < 10 or Wind_speed > 30

print("Can go hiking:", can_go_hiking)
print('Can go swimming:', can_go_swimming)
print("Cannot go outside:", cannot_go_outside)

'''


#Challenge 3:
'''
You're helping a pet shop create a system to determine if they can sell a pet to a customer.

initialize the following variables:

has_license 
has_space 
has_experience 
Write the following logical expressions to determine if:

can_sell_regular_pet: Customer needs EITHER a license OR experience, AND must have space
can_sell_exotic_pet: Customer needs BOTH a license AND experience, AND must have space
cannot_sell_any_pet: Customer has NO license AND NO experience, OR has NO space
'''

''' 
has_license = input('do you have a license? (yes or no): ').lower() == 'yes'
has_space = input('do you hae a space for pet? (yes or no): ').lower() == 'yes'
has_experience = input('do you have experience with pets? (yes or no): ').lower() == 'yes'

can_sell_regular_pet = (has_license or has_experience) and has_space
can_sell_exotic_pet = has_license and has_experience and has_space
cannot_sell_any_pet = not(has_license or has_experience) or not has_space 
print('can sell regular pet?:', can_sell_regular_pet)
print("can sell exotic pet?", can_sell_exotic_pet)
print('cannot sell any pet?', cannot_sell_any_pet)

'''

#Challenge 4:

"""
You're helping a transportation company create a system to determine if a person can drive certain vehicles.

Initialize the following variables:

has_license 
has_experience 
has_clean_record
Write the following logical expressions to determine if:

can_drive_car: Person needs a license AND a clean record
can_drive_truck: Person needs a license AND experience AND a clean record
cannot_drive_any: Person has NO license OR NO clean record
"""

has_license = input('Do you have a license? (yes or no): ').lower() == 'yes'
has_experience = input('Do you have experience? (yes or no): ').lower() == 'yes'
has_clean_record = input('Do you have a clean record? (yes or no): ').lower() == 'yes'

can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = not(has_license and has_clean_record)

print('can drive car:', can_drive_car)
print('can drive truck:', can_drive_truck)
print('cannot drive any:',cannot_drive_any)

