#Polymorphism – operator overloading example

class Book:
    def __init__(self, pages):
        self.pages = pages
        
        
    def __add__(self, other):    #method overloading
        return self.pages + other.pages
    
b1 = Book(100)
b2 = Book(250)

print(b1 + b2)