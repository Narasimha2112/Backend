class Employee:
    company = "Google"       # class variable (shared)
    
    def __init__(self, name):
        self.name = name     # instance variable (unique per object)

e1 = Employee("Raj")
e2 = Employee("Sam")

print(e1.company, e2.company)  # Same for all
print(e1.name)                 # Specific to e1
print(e2.name)                 # Specific to e2
