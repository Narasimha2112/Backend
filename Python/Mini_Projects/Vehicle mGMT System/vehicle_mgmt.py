"""
MINI PROJECT – Vehicle Management System (OOP + Inheritance)
✔ Features:
            Vehicle (parent)
            Car, Bike (child)
            Overriding start() and stop()
            Polymorphism support
"""
from abc import ABC, abstractmethod

#Parent abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
#Child Class-1
class Car(Vehicle):
    def start(self):
        print("Car starting with key....")
        
    def stop(self):
        print("Car Stopped")
        
#Child Class-2
class Bike(Vehicle):
    def start(self):
        print("Bike starting with kick....")
        
    def stop(self):
        print("Bike Stopped")
        
#polymorphism
vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()  #different behavior
    v.stop()