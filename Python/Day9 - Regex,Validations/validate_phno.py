#Validate Phone Number (Indian Format)
import re

phone = input("Enter phone number: ")

pattern = r'^[6-9]\d{9}$'

if re.fullmatch(pattern, phone):
    print("Valid Number")
else:
    print("Invalid Number")