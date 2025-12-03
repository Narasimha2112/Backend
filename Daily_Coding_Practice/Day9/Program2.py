# Validate username (only letters & digits, 5–15 chars)
import re

username = input("Enter username: ")
pattern = r"^[A-Za-z0-9]{5,15}$"

print("Valid" if re.fullmatch(pattern, username) else "Invalid")

