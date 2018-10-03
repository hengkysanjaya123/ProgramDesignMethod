from core import Pet
import time

def main():

    listPets = []

    title = "##############################################################\n" \
            "#                                                            #\n" \
            "#                    Welcome to abc Pet Shops                #\n" \
            "#                                                            #\n" \
            "##############################################################"


    for i in title:
        print(i, end = "")
        if(i != " "):
            time.sleep(0.00000000000000000000000000001)


    while True:
        print()
        print("--------------------------------------------------------------")
        choice = input("What can I help you?\n"
                   "1. Sell Pets\n"
                   "2. Buy Pets\n"
                   "3. View Pets\n"
                   "Enter your choice >>")

        if(choice == "1"):
            name = input("Enter the name (ex : abc, test, etc) >>")
            age = input("Enter the age (ex : 10 , 5, etc) >>")
            type = input("Enter the type (ex: dog, cat, etc) >>")
            color = input("Enter the color (ex : black, white, etc) >>")
            numberOfPets = int(input("Enter the number of pets (ex : 1, 2, etc) >>"))
            price = int(input("Enter the price >>"))


            found = False
            for i in listPets:
                if(i.getName() == name and i.getAge() == age and i.getType() == type and i.getColor() == color):
                    i.setNumberOfPets(int(i.getNumberOfPets()) + numberOfPets)
                    found = True
                    break

            if(found == False):
                pet = Pet(name, age, type, color, numberOfPets)
                listPets.append(pet)

            print("Processing data", end = "")
            for i in range(4):
                print(".", end="")
                time.sleep(0.25)

            print()
            print("Sell Pets sucessful")
            print("You get : "+ str(price * numberOfPets))
            print()

        elif(choice == "2"):
            while True:
                typePet = input("What type of pet you want to buy ?")
                color = input("What color of pet you want to buy ?")

                print("Searching data...", end = "")
                for i in range(4):
                    print(".", end="")
                    time.sleep(0.5)


                tempList = []
                n = 0
                for i in listPets:
                    if(i.getType()== typePet and i.getColor() == color):
                        tempList.append(i)
                    n += 1

                print()
                print()

                if(len(tempList) == 0):
                    print("Sorry, Data not found")
                    print()
                    continue

                print("Available pets : ")

                print("-------------------------------------")
                n = 0
                for i in tempList:
                    print()
                    print(str(n + 1)+".\n"
                          "Name : "+ i.getName() +"\n"
                          "Age : " + i. getAge() +"\n" \
                          "Type : " + i.getType() + "\n"
                          "Color : " + i.getColor() + "\n"
                          "Available : " + str(i.getNumberOfPets())+"\n"
                          "Price (@1): " + str(i.getPrice())
                          )
                    print()
                    n += 1
                print("-------------------------------------")

                choice2 = int(input("Please choose which pets you want to buy (ex : 1)"))

                number = int(input("How many you want to buy ?"))
                selectedPet = tempList[choice2 - 1]
                for i in listPets:
                    if(i == selectedPet):
                        i.setNumberOfPets(int(i.getNumberOfPets()) - number)
                        break

                print("You have to pay : "+ str(int(selectedPet.getPrice()) * number))
                print("Buy Pets successful")
                break
        elif(choice == "3"):

            if(len(listPets) == 0):
                print()
                print("There is no data")
                continue

            print("-------------------------------------")
            n = 0
            for i in listPets:
                print()
                print(str(n + 1)+".\n"
                      "Name : "+ i.getName() +"\n"
                      "Age : " + i. getAge() +"\n" \
                      "Type : " + i.getType() + "\n"
                      "Color : " + i.getColor() + "\n"
                      "Available : " + str(i.getNumberOfPets()) + "\n"
                      "Price (@1): " + str(i.getPrice())
                      )
                print()
                n += 1
            print("-------------------------------------")

main()
