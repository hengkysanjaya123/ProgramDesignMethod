from core import Data

def retrieveData(listData):

    readFile = open('data.txt','r')

    for i in readFile:
        data = i.split(',')
        listData.append(Data(data[0],float(data[1]),int(data[2])))

def writeData(listData):
    write = open('data.txt', 'w')
    for i in listData:
        write.write(f"{i.playerName},{i.averageScore},{i.numberOfPlaying}\n")

    print("Data saved successfully")

def main():

    listData = []

    retrieveData(listData)

    while True:
        print("\n")

        print("Score Record Dota Player\n"
              "========================\n"
              "1. View Record\n"
              "2. Add Player Record\n"
              "3. Add New Player\n"
              "4. Delete Player\n"
              "5. Save and Exit")

        choice = input("Input your choice[1..5]:")

        if (choice == "1"):

            tempArray = []
            for i in listData:
                tempArray.append([i.playerName, i.averageScore, i.numberOfPlaying])


            for i in tempArray:
                print(i)
                # print(str(i).replace("['", "").replace(",", "\t\t\t").replace("'", "").replace("]", ""))

        elif (choice == "2"):
            name = input("Input player name [1..10]:")
            score = int(input("Input player score[0.100]:"))
            idx = -2
            for i in range(len(listData)):
                if (name == listData[i].playerName):
                    idx = i
                    break
            if (idx == -2):
                print(f"name of {name} not found!")
                continue

            current = listData[idx]
            current.averageScore = float((current.averageScore * current.numberOfPlaying + score) / (
                        current.numberOfPlaying + 1))
            current.numberOfPlaying += 1

            print("Score successfully updated ^^")
        elif (choice == "3"):
            name = input("Input player name [1..10]:")

            newData = Data(name, 0,0)
            listData.append(newData)

            print("Data successfully added..")
        elif(choice == "4"):
            name = input("Input player name [1..10]:")
            idx = -2
            for i in range(len(listData)):
                if (name == listData[i].playerName):
                    idx = i
                    break
            if (idx == -2):
                print(f"name of {name} not found!")
                continue

            listData.remove(listData[idx])
            print(f"{name} successfully deleted..")

        elif(choice == "5"):
            writeData(listData)
            break


main()

