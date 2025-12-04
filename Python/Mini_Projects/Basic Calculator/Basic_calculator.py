x = eval(input("Enter First Number: "))
y = eval(input("Enter Second Number:"))

op = input("Enter Operator (+, -, *, /, %, **): ")

if op == "+":
    print(f"{x} + {y} == ",x+y)
elif op == "-":
    print(f"{x} - {y} == ",x-y)
elif op == "*":
    print(f"{x} * {y} == ",x*y)
elif op == "/":
    if y == 0:
        print(f"Error: Division By Zero!!!")
    else:
        print(f"{x} / {y} ==",x/y)
elif op == "%":
    print(f"{x} % {y} == ",x%y)
elif op == "**":
    print(f"{x} ** {y} == ",x**y)
else:
    print(f"Invalid Operator!!!")
    
    