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
print("-----------------------------------------------------")
print("|    Welcome to KMP, type 'back' to back to home    |")
print("-----------------------------------------------------")

while True:
    #ask user to input name
    name = input("Please input name : ")
    #check if the input is back then break
    if(name == "back"):
        break
    #else print the result
    else:
        print(kmp(name))
