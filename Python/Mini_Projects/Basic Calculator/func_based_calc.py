"""
MINI PROJECT – Function Based Calculator

Supports:   Add
            Subtract
            Multiply
            Divide
            Invalid operator handling
            Reusable functions
"""
#Addition
def add(a, b):
    return a + b

#Subtraction 
def sub(a, b):
    return a - b

#Multiply
def mul(a, b):
    return a * b

#Division with Error Handling
def div(a, b):
    if b == 0:
        return "Error : Cannot divide by Zero...."
    return a/b

#Remainder
def rem(a, b):
    return a % b


#Main Logic
num1 = eval(input("Enter the Value for Num1 : "))
num2 = eval(input("Enter the Value for Num2 : "))
op = input("Enter the Operator (+, -, *, /, %) : ")

#Check Operator and Call functions
if op == "+":
    print(f"Sum of {num1} & {num2} are {add(num1,num2)}")
elif op == "-":
    print(f"Difference of {num1} & {num2} are {sub(num1,num2)}") 
elif op == "*":
    print(f"Multiplication of {num1} & {num2} are {mul(num1,num2)}")
elif op == "/":
    print(f"Division of {num1} & {num2} are {div(num1,num2)}")
elif op == "%":
    print(f"Remainder of {num1} & {num2} are {rem(num1,num2)}")
else:
    print("Invalid Operator")