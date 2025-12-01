class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  #private variable
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        
acc = BankAccount(1000)
acc.deposit(5100)
print(acc.get_balance())