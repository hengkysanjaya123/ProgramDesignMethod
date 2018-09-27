#define function
def stones():
    #looping
    while True:
        #ask for input
        num = input("Please Input number : ")
        #if the input is back then break
        if(num == "back"):
            break
        else:
            #cast to integer
            num = int(num)
            #check if even
            if( num % 2 == 0):
                print("Bob")
            # if odd
            else:
                print("Alice")

#print message
print("-----------------------------------------------------------")
print("|    Welcome to AliceNBob, type 'back' to back to home    |")
print("-----------------------------------------------------------")
#call function
stones()
