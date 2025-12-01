#Class to check if number is even/odd

class Number:
    def __init__(self, num):
        self.num = num
        
    def check(self):
        if self.num % 2 == 0:
            return f"Even"
        return f"Odd"


x = int(input("Enter a number: "))
n = Number(x)
print(n.check())