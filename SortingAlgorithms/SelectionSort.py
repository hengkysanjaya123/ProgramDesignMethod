list1 = [64, 25, 12, 22, 11]
# list1 = ["d", "b", "a", "e", "f", "b" ]

def swap(x, y):
    temp = list1[x]
    list1[x] = list1[y]
    list1[y] = temp

for i in range(len(list1)):

    minIdx = i

    for j in range(i + 1, len(list1)):
        if list1[minIdx] > list1[j]:
            minIdx = j

    swap(i, minIdx)

for i in list1:
    print(i, end=",")




