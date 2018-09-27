#import statement
import os
from platform import system as system_name
from os import system as system_call

#define a function to clear screen
def clear_screen():
    #check operation system
    command = "cls" if system_name().lower()=="windows" else "clear"

    # calling
    system_call(command)


#looping
while True:
    #clear the screen
    clear_screen()

    #display message and choice
    print("-----------------Welcome-----------------")
    print("1. KMP")
    print("2. Modul42")
    print("3. AliceNBob")
    print("4. CupsNBall")
    print("5. Exit Application")

    #ask for input
    option = input("Choose your option (1, 2, 3, 4, 5) : ")

    #check input and run the file
    if(option == "1"):
        os.system("python kmp.py")
    elif(option == "2"):
        os.system("python module42.py")
    elif(option == "3"):
        os.system("python AliceNBob.py")
    elif(option == "4"):
        os.system("python CupsNBall.py")
    elif(option == "5"):
        break
    else:
        print("Please enter option correctly")
