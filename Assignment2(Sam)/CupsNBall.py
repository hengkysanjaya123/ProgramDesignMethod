#declare a list to represent the position of ball
ballData = [1,0,0];

#define function
def cupsNBall(stringValue):
    #set the input string to lower case
    stringValue = stringValue.lower()
    #loop for each character from input string
    for i in stringValue:
        #check the character is a or b or c
        # then switch the position of value 1 that represent the position of ball
        if(i == "a"):
            before = ballData[0]
            ballData[0] = ballData[1]
            ballData[1] = before
        elif(i == "b"):
            before = ballData[1]
            ballData[1] = ballData[2]
            ballData[2] = before
        elif(i == "c"):
            before = ballData[0]
            ballData[0] = ballData[2]
            ballData[2] = before

    #loop the data
    for i in range(3):
        #searching the ball position
        if(ballData[i] == 1):
            return i + 1


#display message
print("-----------------------------------------------------------")
print("|    Welcome to CupsNBall, type 'back' to back to home    |")
print("-----------------------------------------------------------")

#looping
while True:
    #ask the user to input step
    stringValue = input("Please input the move step (abc): ")
    stringValue = stringValue.lower()

    #check if the input is 'back' then break
    if(stringValue == "back"):
        break
    else:
        check = True
        # validate if the input is not 'a', 'b', 'c'
        for i in stringValue:
            if(i not in ["a", "b", "c"]):
                print("The move only abc")
                check = False
                break

        #if validated
        if(check):
            #call the function and print the result of ball position
            print(cupsNBall(stringValue))
