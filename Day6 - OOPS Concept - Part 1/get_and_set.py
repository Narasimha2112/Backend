class Product:
    def __init__(self):
        self.__price = 0
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")
            
p = Product()
p.set_price(500)
print(p.get_price())