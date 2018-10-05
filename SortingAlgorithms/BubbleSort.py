list1 = [64, 25, 12, 22, 11]


for i in range(len(list1) -1):
    for j in range(0, len(list1) - i -1):
        if(list1[j] > list1[j + 1]):
            list1[j], list1[j + 1] = list1[j + 1] , list1[j]

print(list1)
