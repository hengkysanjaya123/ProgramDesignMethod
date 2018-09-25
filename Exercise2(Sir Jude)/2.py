# 2.	Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

#define function passing 1 parameter
def getLength(stringValue):
    #declare variable
    counter = 0
    #looping each element in value
    for i in stringValue:
        #increment value with one
        counter = counter +1
    #return value
    return counter

#calling function
print(getLength("hello world"))
print(getLength([5, 3, 6, 7, 9]))
