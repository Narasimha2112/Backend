def greet():
    print("Hello, Welcome!")
    
greet()

#Function With Parameters --> Parameters = input values to function.
def sub(a, b):
    print("subtraction: ",a - b)

sub(10,20)

#Function with return value --> return sends a value back.
def add(a, b):
    return a+b

result = add(5, 10)
print(result)

#Type of Arguments
# 1) Positional Arguments 
def info(name, age):
    print(name, age)
    
info("Venkat", 21)   #Order Matters


# 2) Keyword Arguments
info(age = 23, name = "Rahul")   #Order doesn't matter

# 3) Default Arguments
def greet(name = "Guest"):
    print("Hello", name)
    
greet()  #uses default value
greet("Dhoni")  #Overrides default


# 4) Variable Length Arguments(*args) --> Used for multiple values (tuple).
def total(*nums):
    print(sum(nums))
    
total(10, 20, 30, 40)

# 5) Keyword Variable Arguments(**args) --> Used for key–value pairs (dict).
def display(**data):
    print(data)
    
display(name = "Raj", age = 24)