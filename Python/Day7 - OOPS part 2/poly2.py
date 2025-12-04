class Car:
    def start(self):
        print("Car starts")
    
class Bike:
    def start(self):
        print("Bike starts")
        
def check(vehicle):
    vehicle.start()   #same method name, different behavior
    
c = Car()
b = Bike()

check(c)
check(b)