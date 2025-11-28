# Handle FileNotFoundError

try:
    with open("Unknown.txt", "r") as f:
        print(f.read())
except:
    print("File does not exist.....")