#Create class Car → ElectricCar and override start()

class Car:
    def start(self):
        print("Car starting....")
        
class ElectricCar(Car):
    def start(self):
        print("Electric Car starting silently.....")
        
e = ElectricCar()
e.start()