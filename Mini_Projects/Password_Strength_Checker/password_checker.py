#Mini Project --> Password Strength Checker

"""
✔ Conditions:

length >= 8

contains digits

contains uppercase

contains lowercase

contains special characters

"""

password = input("Enter a Password: ")

has_digits = False
has_uppercase = False
has_lowercase = False
has_special_ch = False

special_chars = "!@#$%^&*()_+"

#Loop each character in password
for ch in password:
    if ch.isupper():   #Check Uppercase
        has_uppercase = True
    elif ch.islower():   #Check Lowercase
        has_lowercase = True
    elif ch.isdigit():   #Check Digits
        has_digits = True
    elif ch in special_chars: #Check Special characters
        has_special_ch = True
        
#Final Strength Check
if len(password) >= 8 and has_uppercase and has_lowercase and has_digits and has_special_ch :
    print("Strong Password 💪")
else:
    print("Weak Password.... ❌")
