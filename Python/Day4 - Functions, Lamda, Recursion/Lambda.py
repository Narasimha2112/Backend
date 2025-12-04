"""
Lambda Functions (Anonymous Functions)

Used for small, one-line functions.

"""
#Basic lambda
square = lambda x : x*x
print(square(10))

#Lambda with multiple arguments
add = lambda a, b : a + b
print(add(5,9))

#Lambda with sorted()
students = [("raj", 21), ("sam", 19), ("john", 25)]

#sorted by age
sorted_list = sorted(students, key=lambda x: x[1])
print(sorted_list)