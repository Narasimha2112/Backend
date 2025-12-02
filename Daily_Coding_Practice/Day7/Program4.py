#Using Super
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        super().show()
        print("B class")

b = B()
b.show()
