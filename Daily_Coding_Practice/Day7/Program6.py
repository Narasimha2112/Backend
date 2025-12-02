#Multiple Inheritance

class X:
    def fx(self):
        print("X")
        
class Y:
    def fy(self):
        print("Y")
        
class Z(X, Y):
    pass

z = Z()
z.fx()
z.fy()