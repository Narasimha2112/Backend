class Bird:
    def fly(self):
        print("Bird can fly")
        
class Penguin(Bird):
    def fly(self):
        print("Penguin Cannot fly")

b1 = Bird()
b2 = Penguin()

b1.fly()
b2.fly()