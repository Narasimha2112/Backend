#Create class using private variable (age)
class Person:
    def __init__(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

p = Person(25)
print(p.get_age())
