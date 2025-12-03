# Check if string contains only alphabets
import re

text = input("Enter: ")

print("Valid" if re.fullmatch(r"[A-Za-z]+", text) else "Invalid")