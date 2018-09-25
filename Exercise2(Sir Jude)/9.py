#9.	Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.

#declare function
def maps(listString):
    #declare a list variable
    data = []
    #looping element in listString
    for i in listString:
        #append length of i to data
        data.append(len(i))

    return data


#calling function
print(maps(["abc", "test", "jklasdf"]))
