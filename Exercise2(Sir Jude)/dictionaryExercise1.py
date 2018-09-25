import pprint

allGuest = { "Hengky" : { 'beer' : 6 , 'pizza' : 20, 'lumpia' : 10},
             "Nico" : {'dimsum' : 2 , 'lumpia' : 1},
             "Rino" : { 'beer' : 5}
           }

def totalBrought(guests):
    foodDict = {}
    for i in guests.keys():
        # i = Hengky , Nico, Rino
        for j in guests[i].keys():
            # j = beer, pizza, lumpia, dimsum
            foodDict.setdefault(j, 0)
            foodDict[j] = foodDict[j] + guests[i].get(j)

    pprint.pprint(foodDict)

totalBrought(allGuest)



# solution 2
def totalBrought2(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print(totalBrought2(allGuest, 'beer'))
