#Validate Pin code (6 digits, start 1-9)

import re

pincode = input("Enter pin: ")

pattern = r"^[1-9]\d{6}$"

print("Valid" if re.fullmatch(pattern, pincode) else "Invalid")