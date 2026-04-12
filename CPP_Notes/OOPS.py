##Encapsulation:

class Encapsulation:
    def __init__(self):
        self.__balance = 0

    def deposit_amount(self,amount):
        if(amount>0):
            self.__balance += amount    

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = Encapsulation()
    account.get_balance()             