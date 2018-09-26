#define function
def kmp(stringValue):
    #split the string by strip
    data = stringValue.split("-")
    #declare variable to store the result
    result = ""

    #loop the data
    for i in data:
        #store it into data
        result = result + i[0].upper()
    return result

#calling
print(kmp("Pasko-Patak"))
