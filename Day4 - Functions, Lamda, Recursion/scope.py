"""
Two types of scopes 1)Local Scope
                    2)Global Scope
"""

#Local Scope
def func():
    x = 10  #local variable
    print(x)
    
func()

#Global scope
y = 50 #Global Variable

def show():
    print(y)
    
show()
