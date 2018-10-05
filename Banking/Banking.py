from core import Account
from core import Customer
from core import Bank

import time


def displayListBank(listBank):
    print()
    print("List available bank : ")
    n = 1
    for i in listBank:
        print(str(n) + ". " + i.getBankName())
        n = n + 1

    print()

def main():

    listBank = []
    listCustomer = []
    idxBank = 0

    print("********************************************************************************\n"
          "*                                                                              *\n"
          "*                   Welcome to many many bank in one machine                   *\n"
          "*                                                                              *\n"
          "********************************************************************************")

    while True:
        print("#############################################################################")

        choice = input("Login as (Admin/User/Exit) >>").lower()

        statusLoadOperation = True
        if(choice == "admin"):
            while True:
                choiceBank = input("\n-------------------------------------\n"
                                   "1. Create new bank\n"
                                    "2. Display list bank\n"
                                    "3. Logout\n"
                                    "Enter your choice >>")

                if(choiceBank == "1"):
                    bank = Bank(input("Enter bank's name >>"))
                    listBank.append(bank)
                    idxBank = len(listBank) - 1

                    print("Creating bank", end="")
                    for i in range(4):
                        print(".", end="")
                        time.sleep(0.25)
                    print()
                    print("~~ Bank created successfully ~~")
                    continue
                elif(choiceBank == "2"):
                    displayListBank(listBank)
                    continue
                elif(choiceBank == "3"):
                    statusLoadOperation = False
                    break

        elif(choice == "user"):

            while True:
                choiceBank = input("\n-------------------------------------\n"
                                   "1. Search bank\n"
                                   "2. Display list bank\n"
                                   "3. Logout\n"
                                   "Enter your choice >>")

                if(choiceBank == "1"):
                    found = False
                    name = input("Enter bank's name >>")
                    n = 0
                    for i in listBank:
                        if(i.getBankName() == name):
                            idxBank = n
                            found = True
                            break
                        n+=1
                    if(found == False):
                        print("~~ Bank not found ~~")
                        continue
                    else:
                        break

                elif(choiceBank == "2"):
                    displayListBank(listBank)
                    continue
                elif(choiceBank == "3"):
                    statusLoadOperation = False
                    break
        elif(choice == "exit"):
            print("~~ Thank you ~~")
            break
        else:
            print("~~ Please enter Admin / User ~~")
            continue

        if(statusLoadOperation):
            LoadOperation(idxBank, listBank, listCustomer)


def LoadOperation(idxBank, listBank, listCustomer):
    print()
    currentBank = listBank[idxBank]
    print("--------------------------------------------------------\n"
          "Welcome to " + currentBank.getBankName())
    print()
    while True:
        choice = input("--------------------------------------------------------\n"
                       "1. Create new account\n"
                       "2. Searching account\n"
                       "3. Logout\n"
                       "Enter your choice >>")

        print()

        customerIdx = 0
        if (choice == "1"):
            print("Please fill some information to create new account")
            time.sleep(0.5)
            print()

            fName = input("Enter Firstname >>")
            lName = input("Enter Lastname >>")

            currentBank.addCustomer(fName, lName)
            cust1 = currentBank.getCustomer(currentBank.getNumOfCustomers() - 1)

            amt = int(input("Enter Amount >>"))
            cust1.setAccount(Account(amt))

            listCustomer.append(cust1)
            customerIdx = len(listCustomer) - 1

            print("Creating account")
            for i in range(4):
                print(".", end="")
                time.sleep(0.5)
            print()

            print("Create Account success")
            print()
        elif (choice == "2"):
            founded = False
            fName = input("Enter Firstname >>")
            lName = input("Enter Lastname >>")

            n = 0
            for i in listCustomer:
                if (i.getFirstName() + " " + i.getLastName() == fName + " " + lName):
                    customerIdx = n
                    founded = True
                    break
                n += 1

            if (founded == False):
                print()
                print("There is no data founded")
                continue

            print("Searching data")
            for i in range(4):
                print(".", end="")
                time.sleep(0.5)
            print()

            print("Data founded")
            print()
        elif (choice == "3"):
            break

        currentCustomer = listCustomer[customerIdx]
        acc = currentCustomer.getAccount()

        while True:
            print(".....................................................................")
            choice = input("1. Balance Inquiry\n"
                           "2. Deposit\n"
                           "3. Withdraw\n"
                           "4. Back\n"
                           "Enter your choice >>")
            if (choice == "1"):
                print("Full name : " + currentCustomer.getFirstName() + " " + currentCustomer.getLastName() + "\n"
                                                                                                              "Balance : " + str(
                    acc.getBalance())
                      )
            elif (choice == "2"):
                amt = int(input("Enter amount to deposit >>"))
                acc.deposit(amt)

                print("processing data", end="")
                for i in range(4):
                    print(".", end="")
                    time.sleep(0.5)

                print()
                print("Deposit Success")
            elif (choice == "3"):
                amt = int(input("Enter amount to withdraw >>"))
                acc.withdraw(amt)

                print("processing data", end="")
                for i in range(4):
                    print(".", end="")
                    time.sleep(0.5)

                print()
                print("Withdraw Success")
            elif (choice == "4"):
                break

            print()
            print("***************************************************************************************************")
            print()


main()

