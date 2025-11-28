# Exception Handling (try / except / else / finally)

#basic try-except
try:
    a = 10 / 5
    print(a)
except ZeroDivisionError:
    print("You cannot divide by zero")
    

#Multiple Exceptions
try:
    x = int("abc")
except ValueError:
    print("Invalid Integer")
    

#try + except + else
try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid Integer")
else:
    print("You Entered:",n)


# try + finally(runs always)
try:
    f = open("data.txt")
    print("File Opened")
finally:
    print("Finally block Executed")