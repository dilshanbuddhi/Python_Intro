class Car:
    def __init__(self, brand):
        self.__brand = brand

    def get_display(self):
        print(self.__brand)

car = Car("GTR")
print(car.get_display())


"""
define a py class band account that models the basic bank account using a consept of encapsulation
your class should

use private attribute for account number , owner name , balance should start 0.1 by default
provide a constructor that accept only account number and name 

the banance should be initializr to 0.0 inside the constructor

include the following public method 
   display_acc() print the owners name and current value ( but not the acc num )
   deposit add a money to the account only if the amount is valid  
   
withdraw amount - dedux money only if there is enough value
get_balance - return the current value 

implement a private method call validate amount that 
    returns true if a amount is a positive number 
    is used internally by both deposit() and withdraw()to validate 
    
"""

class BankAccount :
    def __init__(self , acc_num , owner_name ):
        self.__acc_num = acc_num,
        self.__owner_name = owner_name
        self.__balance = 0.0

    def display_acc (self):
        print(f"name : {self.__owner_name} \n balance : {self.__balance}")

    def deposit(self , amount):
        if self.__validate_amount(amount):
            self.__balance += amount
        else:
            print("invalid amount")

    def withdraw(self , amount):
        if self.__validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("invalid amount")

    def get_balance(self):
        return self.__balance

    def __validate_amount(self , amount):
        return amount > 0


bankAccount = BankAccount("1234" , "mmmmmm")
bankAccount.display_acc()

bankAccount.deposit(1000)

bankAccount.withdraw(500)

bankAccount.display_acc()



print(bankAccount.get_balance())
