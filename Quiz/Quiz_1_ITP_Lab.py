refreDict = { "top" : {}, "middle" : {} , "bottom" : {}}

#this function is to get the available space
def getNumberOfStuff(spacePosition):
    if(spacePosition == "top"):
        total = 0
        for i in refreDict["top"].keys():
            total = total + int(refreDict["top"].get(i))
        return total
    elif(spacePosition == "mid"):
        total = 0
        for i in refreDict["middle"].keys():
            total = total + int(refreDict["middle"].get(i))
        return total
    elif(spacePosition ==  "bottom"):
        total = 0
        for i in refreDict["bottom"].keys():
            total = total + int(refreDict["bottom"].get(i))
        return total


print("----------Welcome to refrigerator----------")
topSpace = int(input("input the maximum of available space in top : "))
middleSpace = int(input("input the maximum of available space in middle : "))
bottomSpace = int(input("input the maximum of available space in bottom : "))


while True:
    operation = input("Do you want to Take out / Put things into the refrigerator ? Y/N")
    operation = operation.lower()

    if(operation[0] == "y"):
        action = input("Choose an Action: PUT/TAKE/VIEW")
        action = action.lower()

        if(action == "view"):
            for i in refreDict.keys():
                print("----------------"+ i + "----------------")
                print()
                for j in refreDict[i].keys():
                    print("Items : " + j + " | Volume : " + str(refreDict[i].get(j)))
                print()
            continue

        spacePosition = input("Pick Space TOP/MID/BOTTOM")

        if(action == "put"):
            stuff = input("What do you want to put in?")
            volume = int(input("Volume of Item : "))

            available = 0
            if(spacePosition == "top"):
                available = topSpace
            elif(spacePosition == "mid"):
                available = middleSpace
            elif(spacePosition == "bottom"):
                available = bottomSpace

            numberOfStuff = getNumberOfStuff(spacePosition)

            available = available - numberOfStuff

            if(volume > available):
                print("Sorry, not enough space \nThe available space is : "+ str(available))
            else:
                if(spacePosition == "top"):
                    refreDict["top"].setdefault(stuff, 0)
                    refreDict["top"].update({ stuff : refreDict["top"].get(stuff) + volume})
                elif(spacePosition == "mid"):
                    refreDict["middle"].setdefault(stuff, 0)
                    refreDict["middle"].update({ stuff : refreDict["middle"].get(stuff) + volume})
                elif(spacePosition == "bottom"):
                    refreDict["bottom"].setdefault(stuff, 0)
                    refreDict["bottom"].update({ stuff : refreDict["bottom"].get(stuff) + volume})
        elif(action == "take"):
            stuff = input("What do you want to take in?")
            volume = int(input("Volume of Item : "))

            if(spacePosition == "top"):

                if(stuff not in refreDict["top"].keys()):
                    print("You dont have " + stuff + " in your refrigerator")
                    continue

                if(volume > refreDict["top"].get(stuff)):
                    print("You just have " + str(refreDict["top"].get(stuff)) + " inside your refrigerator")
                    continue

                refreDict["top"].setdefault(stuff, 0)
                refreDict["top"].update({ stuff : refreDict["top"].get(stuff) - volume})
            elif(spacePosition == "mid"):
                if(stuff not in refreDict["middle"].keys()):
                    print("You dont have " + stuff + " in your refrigerator")
                    continue

                if(volume > refreDict["middle"].get(stuff)):
                    print("You just have " + str(refreDict["middle"].get(stuff)) + " inside your refrigerator")
                    continue

                refreDict["top"].setdefault(stuff, 0)
                refreDict["top"].update({ stuff : refreDict["middle"].get(stuff) - volume})
            elif(spacePosition == "bottom"):

                if(stuff not in refreDict["bottom"].keys()):
                    print("You dont have " + stuff + " in your refrigerator")
                    continue

                if(volume > refreDict["bottom"].get(stuff)):
                    print("You just have " + str(refreDict["bottom"].get(stuff)) + " inside your refrigerator")
                    continue

                refreDict["top"].setdefault(stuff, 0)
                refreDict["top"].update({ stuff : refreDict["bottom"].get(stuff) - volume})

        print(refreDict)
    else:
        break
