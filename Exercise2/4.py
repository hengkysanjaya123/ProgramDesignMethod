#solution 1
def reverse(stringValue):
    data = list(stringValue)
    x= data[::-1]
    return (''.join(x))

#solution 2
def reverse2(stringValue):
    data = ""
    for i in range(len(stringValue)-1, -1 ,-1):
        data = data + stringValue[i]
    return data

print(reverse("I am testing"))
print(reverse2("I am testing"))
