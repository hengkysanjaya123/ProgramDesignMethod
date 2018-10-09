class Account:
    # __balance = 0

    def __init__(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def deposit(self, amt):
        if(amt < 0):
            return False
        else:
            self.__balance += amt

    def withdraw(self, amt):
        if(amt <0 or amt > self.__balance):
            return False
        else:
            self.__balance -= amt
            return True

class Customer:
    # __firstName = ""
    # __lastName = "",
    # __account = ""

    def __init__(self, firstname, lastname):
        self.__firstName = firstname
        self.__lastName = lastname

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAccount(self):
        return self.__account

    def setAccount(self, account):
        self.__account = account


class Bank:
    __customer = []
    __numberOfCustomer = 0
    __bankName = ""

    def __init__(self ,bankName):
        self.__bankName = bankName

    def addCustomer(self, firstname, lastname):
        cust1 = Customer(firstname, lastname)
        self.__customer.append(cust1)
        self.__numberOfCustomer += 1

    def getNumOfCustomers(self):
        return self.__numberOfCustomer

    def getCustomer(self, idx):
        return self.__customer[idx]

    def getBankName(self):
        return self.__bankName
