class Animal:
    def sound(self):
        print("Animals Makes sound")
        
class Dog(Animal):
    def sound(self):             #method Overriding
        print("Dog Barks")
        
d = Dog()
d.sound()