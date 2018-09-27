#define function
def modulo():
    #create empty dictionary
    dict = {}
    #loop until 10
    for i in range(10):
        #ask for input for each iteration
        number = input("Please input a number "+str(i + 1)+": ")

        #check if input is back then break
        if(number == "back"):
            break
        #else then parse to integer
        else:
            number = int(number)

        #get the remaining value of number divide by 42
        mod = number % 42
        #set default value to dictionary
        dict.setdefault(mod, 0)
        #add 1 to the value
        dict[mod] = dict[mod] + 1
    return len(dict)


#display message
print("----------------------------------------------------------")
print("|    Welcome to Modulo42, type 'back' to back to home    |")
print("----------------------------------------------------------")

#call the function and print it
print("Result : "+str(modulo()))
