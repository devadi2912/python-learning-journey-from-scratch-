"""
Problem 1: Bank Account 💰

Create a BankAccount class with the following requirements:

Initialize the account holder's name and balance using __init__().
Create a getter for the balance.
Create a setter for the balance that rejects negative values.
If the balance is negative, print "Invalid balance!" without updating it.

Expected behaviour:

account = BankAccount("Aditya", 5000)

print(account.balance)  # 5000

account.balance = 8000
print(account.balance)  # 8000

account.balance = -200
print(account.balance)  # 8000
"""

class Bank :
    def __init__(self, name, balance):
        self.name = name 
        self._balance = balance
    
    @property 
    def balance (self):
        return self._balance 
    
    @balance.setter 
    def balance (self, balance):
        if ( balance < 0 ):
            print ("invalid input! for balance")
        else :
            self._balance = balance 
            
acc1 = Bank("aditya", 5000)

print (acc1.balance)
acc1.balance =  int(input("enter the new value for balance :"))
print (acc1.balance)
acc1.balance =  int(input("enter negative value for balance :"))
print (acc1.balance)
