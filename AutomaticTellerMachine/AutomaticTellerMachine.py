import time

class Account:
    __balance = 0
    __accountNumber = 0
    __accountName = ""

    def __init__(self, accountNumber, accountName,balance = 0):
        self.__balance = balance
        self.__accountNumber = accountNumber
        self.__accountName = accountName


    def deposit(self, amt):
        if amt < 0:
            return False
        else:
            self.__balance += amt
            return True

    def withdraw(self, amt):
        if(amt > self.__balance or amt < 0):
            return False
        else:
            self.__balance -= amt
            return True

    def balanceInqury(self):
        return self.__balance

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountName(self):
        return self.__accountName

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setAccountName(self, accountName):
        self.__accountName = accountName

    def getInformation(self):
        return "Account Name : "+ self.__accountName +"\n" \
               "Account Number : " + self.__accountNumber +"\n" \
               "Balance : " + str(self.__balance)


def searchAccount(accountData,accountNumber):
    n = 0
    for i in accountData:
        if(i.getAccountNumber() == accountNumber):
            return n
        n +=1


def main():

    accountData = []

    while True:
        print("---------Welcome to ABC Automatic Teller Machine---------")
        print("1. Create new Account\n"
              "2. Search Account\n"
              "3. Exit")

        idx = 0

        choice = input("Please enter your choice >>")
        if(choice == "1"):
            accountName = input("Please enter your account name >>")
            accountNumber = input("Please enter your account number >>")

            print("Creating account...")
            time.sleep(1)

            acc1 = Account(accountNumber, accountName)
            accountData.append(acc1)
            idx = len(accountData) -1

            print("Account created successfully")
        elif(choice == "2"):
            accountNumber = input("Please enter your account number >>")
            idx = searchAccount(accountData, accountNumber)

            print("Getting data...")
            time.sleep(0.5)
        elif(choice == "3"):
            break

        print("***********************************************************************************************************************")

        try:
            currentAccount = accountData[idx]
        except TypeError:
            print("Account number not found")
            continue


        print()

        while True:
            print("1. Balance Inquiry\n"
              "2. Deposit\n"
              "3. Withdraw\n"
              "4. Display Account\n")
            choice = input("Please enter your choice >>")
            if(choice == "1"):
                print("Getting data...")
                time.sleep(0.5)

                print("Your balance is : "+ str(currentAccount.balanceInqury()))

                time.sleep(0.5)
            elif(choice == "2"):
                amt = int(input("Please enter amount >>"))
                currentAccount.deposit(amt)

                print("Processing data...")
                time.sleep(0.5)
            elif(choice == "3"):
                amt = int(input("Please enter amount >>"))
                currentAccount.withdraw(amt)

                print("Processing data...")
                time.sleep(0.5)
            elif(choice == "4"):
                print("Getting data...")
                time.sleep(0.5)

                print(currentAccount.getInformation())

            print()
            print("Operation success")
            print("***********************************************************************************************************************")
            action = input("Do you want to do another operation ? (Y/N)").lower()
            if(action == "n"):
                break

main()
