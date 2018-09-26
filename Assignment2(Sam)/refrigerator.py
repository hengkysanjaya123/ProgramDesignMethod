topSpace = 15
middleSpace = 50
bottomSpace = 0
refriDic = { "top" : {"fish" : 1}, "middle" : {}, "bottom" : {}}

def getSpace(spacePosition):
    if(spacePosition == "top"):
        total = 0
        for i in refriDic["top"].keys():
            total = total + int(refriDic["top"].get(i))
        return topSpace - total
    elif(spacePosition == "mid"):
        total = 0
        for i in refriDic["middle"].keys():
            total = total + int(refriDic["middle"].get(i))
        return middleSpace - total
    elif(spacePosition == "bottom"):
        total = 0
        for i in refriDic["bottom"].keys():
            total = total + int(refriDic["bottom"].get(i))
        return bottomSpace - total



print("Welcome to the Refrigerator")

while True:
    operation = input("Do you want to take out/put in things into the refrigerator? Y/N")
    operation = operation.lower()

    if(operation == "y"):
        action = input("Choose an Action: PUT/TAKE/VIEW")
        action = action.lower()

        if(action == "view"):
            print()
            print("There are inside my refrigerator : ")
            for i in refriDic.keys():
                print("-----------"+i+"-----------")
                for j in refriDic[i].keys():
                    print(str(refriDic[i].get(j)) + " " + j)
            print()
            continue


        spacePosition = input("Pick space TOP/MID/BOTTOM:")
        spacePosition = spacePosition.lower()

        availableSpace = getSpace(spacePosition)

        if(action == "put"):
            stuff = input("What do you want to put in?")
            volume = int(input("Volume of item : "))

            if(volume > availableSpace):
                print("Sorry, you cannot add "+str(volume) + " item of "+stuff+"\nThe available space is : "+ str(availableSpace))
                continue
            else:
                if(spacePosition == "top"):
                    refriDic["top"].setdefault(stuff,0)
                    refriDic["top"].update({stuff : refriDic["top"].get(stuff) + volume})
                elif(spacePosition == "mid"):
                    refriDic["middle"].setdefault(stuff,0)
                    refriDic["middle"].update({stuff : refriDic["middle"].get(stuff) + volume})
                elif(spacePosition == "bottom"):
                    refriDic["bottom"].setdefault(stuff,0)
                    refriDic["bottom"].update({stuff : refriDic["bottom"].get(stuff) + volume})
        elif(action == "take"):
            stuff = input("What do you want to take in?")

            if(spacePosition == "top"):
                if(stuff not in refriDic["top"]):
                    print("There is no "+ stuff + " inside refrigerator")
            elif(spacePosition == "mid"):
                if(stuff not in refriDic["middle"]):
                    print("There is no "+ stuff + " inside refrigerator")
            elif(spacePosition == "bottom"):
                if(stuff not in refriDic["bottom"]):
                    print("There is no "+ stuff + " inside refrigerator")

            volume = int(input("Volume of item : "))



            if(volume > availableSpace):
                print("Sorry, you cannot add "+str(volume) + " "+stuff+"\nThe available space is : "+ str(availableSpace))
                continue
            else:
                if(spacePosition == "top"):
                    refriDic["top"].setdefault(stuff,0)
                    refriDic["top"].update({stuff : refriDic["top"].get(stuff) - volume})
                elif(spacePosition == "mid"):
                    refriDic["middle"].setdefault(stuff,0)
                    refriDic["middle"].update({stuff : refriDic["middle"].get(stuff) - volume})
                elif(spacePosition == "bottom"):
                    refriDic["bottom"].setdefault(stuff,0)
                    refriDic["bottom"].update({stuff : refriDic["bottom"].get(stuff) - volume})
        else:
            continue

    elif (operation == "n"):
        break
