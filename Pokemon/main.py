from core import Pokemon, Water, Fire

def getDataFromFile(file, list):
    
    try:
        header = next(file)
    except:
        print("no data in file")
    
    for i in file:
        data = i.replace('\n','').split(',')
        if(data[6] == "water"):
            water = Water(data[1], data[2], data[3], data[4]  , data[5], data[6])
            list.append(water)
        elif(data[6] == "fire"):
            fire = Fire(data[1], data[2], data[3], data[4]  , data[5], data[6])
            list.append(fire)


def main():
    file = open('data.txt', 'r+')

    listPokemon = []


    getDataFromFile(file, listPokemon)

    while True:
        print()
        print("Welcome to Pokemon")
        print("-----------------------")
        choice = input("1. Add Pokemon\n"
                       "2. Edit\n"
                       "3. Delete\n"
                       "4. Search\n"
                       "5. Save to File\n"
                       "6. Display\n"
                       "7. Exit\n"
                       "Enter your choice >>")

        if(choice == "1"):
            type = input("Enter the type>>")
            name = input("Enter the name >>")
            hp = input("Enter hp >>")
            attackStat = input("Enter the attack stat >>")
            defenseStat = input("Enter the defense Stat >>")
            moveSet = input("Enter the move set>>")

            if(type == "water"):
                weight = input("Enter the weight >>")
                water = Water(name, hp, attackStat, defenseStat  , moveSet, type,weight)
                listPokemon.append(water)
            elif(type == "fire"):
                height = input("Enter the height >>")
                fire = Fire(name, hp, attackStat, defenseStat  , moveSet, type,height)
                listPokemon.append(fire)

            print("~~ Data Added Successfully ~~")
        elif (choice == "2"):
            name = input("Enter the name >>")
            currentIdx = 0
            for i in range(len(listPokemon)):
                if(listPokemon[i].getName() == name):
                    currentIdx = i
                    break

            powerUp = int(input("Enter the power up value >>"))
            evolve = int(input("Enter the evolve value >>"))

            current = listPokemon[currentIdx]
            current.powerUp(powerUp)
            current.evolve(evolve)
            listPokemon[i] = current

            print("~~ Data Edit Successfully ~~")
        elif (choice == "3"):
            name = input("Enter the name >>")
            currentIdx = 0
            for i in range(len(listPokemon)):
                if(listPokemon[i].getName() == name):
                    currentIdx = i
                    break

            listPokemon.remove(listPokemon[currentIdx])

            print("~~ Data Deleted Successfully ~~")

        elif (choice == "4"):
            name = input("Input the pokemon name you want to search >>")
            for i in range(len(listPokemon)):
                print(listPokemon[i].getName())
                if(listPokemon[i].getName() == name):
                    cur = listPokemon[i]
                    print(str(i+1) + "----------------------------")
                    print("Name : " + cur.getName())
                    print("Hp : " + cur.getHp())
                    print("Attack Stat : " + cur.getAttackStat())
                    print("Defense Stat : " + cur.getDefenseStat())
                    print("Move set : " + cur.getMoveSet())
                    print("Type : " + cur.getType())
                    print("\n\n")

        elif (choice == "5"):
            write = open('data.txt', 'w')
            n = 1
            result = "No,Name,Hp,AttackStat,DefenseStat,MoveSet,Type\n"
            print(len(listPokemon))
            for i in listPokemon:
                result += str(n) + ","+ i.getName() + "," + i.getHp() + "," + i.getAttackStat() + "," + i.getDefenseStat() + "," + i.getMoveSet() + "," + i.getType() + "\n"
                n += 1

            write.write(result)
            write.close()

            print("~~ Save to file success ~~")
        elif ( choice == "6"):
            n = 1
            print("No,Name,Hp,AttackStat,DefenseStat,MoveSet,Type")
            for i in listPokemon:
                print(str(n) + ","+ i.getName() + "," + i.getHp() + "," + i.getAttackStat() + "," + i.getDefenseStat() + "," + i.getMoveSet() + "," + i.getType())
                n += 1
        elif (choice == "7"):
            break

main()
