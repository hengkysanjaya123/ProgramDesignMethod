def getLength(stringValue):
    counter = 0
    for i in stringValue:
        counter = counter +1
    return counter

print(getLength("hello world"))
print(getLength([5, 3, 6, 7, 9]))
