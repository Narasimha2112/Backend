""" 
MINI PROJECT – Login Form Validator 
👉 Validate:
            username
            email
            password
            phone
"""
import re

def validate_username(u):
    return re.fullmatch(r"[A-Za-z0-9_]{4,12}", u)

def validate_email(e):
    return re.fullmatch(r"[A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}", e)

def validate_password(p):
    return re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}", p)

def validate_phone(ph):
    return re.fullmatch(r"[6-9]\d{9}", ph)


username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")
phone = input("Enter phone: ")

if validate_username(username):
    print("✔ Valid Username")
else:
    print("✖ Invalid Username")

if validate_email(email):
    print("✔ Valid Email")
else:
    print("✖ Invalid Email")

if validate_password(password):
    print("✔ Strong Password")
else:
    print("✖ Weak Password")

if validate_phone(phone):
    print("✔ Valid Phone Number")
else:
    print("✖ Invalid Phone Number")

