import bcrypt

password = "mypassword".encode()

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)