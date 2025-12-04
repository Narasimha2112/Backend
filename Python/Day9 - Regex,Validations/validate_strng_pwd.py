"""Validate Strong Password

Conditions:
✔ 8 characters
✔ uppercase
✔ lowercase
✔ digit
✔ special character
"""

import re

password = input("Enter Password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

if re.fullmatch(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
    
