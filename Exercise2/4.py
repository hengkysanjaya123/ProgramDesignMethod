#4.	Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

#solution 1
def reverse(stringValue):
    # convert inputed value to list
    data = list(stringValue)
    #reverse the array
    x= data[::-1]
    #return the reversed array and join to become string
    return (''.join(x))

#solution 2
def reverse2(stringValue):
    #declare variable
    data = ""
    #looping from the end to start
    for i in range(len(stringValue)-1, -1 ,-1):
        #stored into variable data
        data = data + stringValue[i]
    #return the data
    return data

#calling function
print(reverse("I am testing"))
print(reverse2("I am testing"))
