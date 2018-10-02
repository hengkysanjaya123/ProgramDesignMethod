class Account:
    balance = 0

    def __init__(self, balance):
        self.balance = balance


    def deposit(self, amt):
        if(amt < 0):
            return False
        else:
            self.balance += amt
            return True

    def withdraw(self, amt):
        if(amt > self.balance):
            return False
        else:
            if(amt < 0):
                return False
            else:
                self.balance -= amt
                return True

acc1 = Account(5000)
print(acc1.balance)


acc1.withdraw(5000)
# acc1.deposit(2000)
print(acc1.balance)

# acc2 = Account(2000)
# print(acc2.balance)
