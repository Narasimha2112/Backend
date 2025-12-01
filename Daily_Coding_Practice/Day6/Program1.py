# Create a class Person with name & age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
p = Person("Ravi", 22)
p.display()