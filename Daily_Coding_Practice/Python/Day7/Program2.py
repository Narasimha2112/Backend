# Multilevel Inheritance – A → B → C

class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")
        
obj = C()

obj.showA(), obj.showB(), obj.showC()