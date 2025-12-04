#Single Inheritance – Person → Student
class Person:
    def details(self):
        print("I am a Person")
        
class Student(Person):
    def details(self):
        print("I am a Student")
        
s = Student()
s.details()

p= Person()
p.details()