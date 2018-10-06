"""
bubble sort

loop from first element until last two element
then swap the element with next element
until the greatest move to the right
and lock the greatest element in the right

"""


# list1 = [64, 25, 12, 22, 11]
list1 = ["d", "b", "a", "e", "f", "b" ]

for i in range(len(list1) -1):
    for j in range(0, len(list1) - i -1):
        if(list1[j] > list1[j + 1]):
            list1[j], list1[j + 1] = list1[j + 1] , list1[j]

print(list1)
