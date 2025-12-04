#Abstract Class Example

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Square(Shape):
    def area(self):
        return 5 * 5
    
s = Square()
print(s.area())