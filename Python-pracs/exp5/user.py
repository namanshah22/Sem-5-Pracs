class InvalidAge(Exception):
    message = 'Custom error'

age = 18

try:
    entered_age = int(input("Enter age: "))
    if entered_age < age:
        raise InvalidAge('Less than 18')
except InvalidAge as ce:
    print(ce)
