#Class Calculator

class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            return "Error"
        return a / b
    
c = Calculator()
print(c.add(5,6))
print(c.sub(6,1))
print(c.mul(5,4))
print(c.div(5,0))
print(c.div(90,4))