class Animal:
    def sound(self):
        print("Animal Sound")
        
class Dog(Animal):
    def sound(self):
        super().sound()  #Calling parent class
        print("Dog Barks")

d = Dog()
d.sound()