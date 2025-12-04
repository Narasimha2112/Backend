class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
c = Car("Tesla", "Model 3")
print(c.full_name())