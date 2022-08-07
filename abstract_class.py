from abc import ABC, abstractmethod

class Bank(ABC):
    def basicinfo():
        print('This is a generic bank')
        return 'Generic bank: 0'
    
    @abstractmethod
    def withdraw():
        pass

class Swiss(Bank):
    def __init__(self, bal) -> None:
        self.bal = 1000
    
    def basicinfo(self):
        print ('This is the Swiss Bank')
        return 'Swiss Bank: ' + str(self.bal)
    
    def withdraw(self, amount):
        if amount > self.bal:
            print('Insufficient funds')
        else:
            self.bal -= amount
            print('Withdrawn amount: ' + str(amount))
            print('New balance: ' + str(self.bal))
        return self.bal