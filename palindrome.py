# import random
#
# def randMe(num):
#     for i in range(num):
#         print(random.randint(1, 10))
#
# randMe(10)


# def readInput():
#     while True:
#         x = input("Please input something : ").lower()
#         if(x == "exit"):
#             break
#
# readInput()


def palindrome(stringValue):
    data = ""
    for i in range(len(stringValue)-1,-1, -1):
        data = data + stringValue[i]
    return data == stringValue

print(palindrome("naman"))
