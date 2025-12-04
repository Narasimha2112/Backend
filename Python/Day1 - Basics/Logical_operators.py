"""
Logical Operators:-

1) And = It returns True when both conditions are true.
2) Or = It returns True atleast one condition is true.
3) Not = It returns Opposite
"""

a = eval(input("Enter the 1st Value: "))
b = eval(input("Enter the 2nd Value: "))

#And Operator
print(a>b and b<a)

#or Operator
print(a>b or b==a)

#Not Operator
print(not a>b)