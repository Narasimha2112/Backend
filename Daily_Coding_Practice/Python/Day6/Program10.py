#Bank Account - Deposit & Withdraw

class Bank:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Insufficient Funds")
        
    def get_balance(self):
        return self.__balance
    
b = Bank(1000)
b.deposit(549)
b.withdraw(1649)
print(b.get_balance())