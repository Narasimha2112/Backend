#Create a class Circle to compute area

class Circle:
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
c = Circle(5)
print(c.area())