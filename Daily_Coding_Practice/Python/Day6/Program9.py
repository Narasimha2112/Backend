#Student marks average using class
class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student([80, 90, 70])
print(s.average())
