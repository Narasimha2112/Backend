#Create Employee class with salary increment
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def increment(self, amount):
        self.salary += amount

e = Employee("Ravi", 5000)
e.increment(4216)
print(e.salary)