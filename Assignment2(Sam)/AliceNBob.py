def stones():
    while True:
        num = input("Please Input number : ")
        if(num == "exit"):
            break
        else:
            num = int(num)
            if( num % 2 == 0):
                print("Bob")
            else:
                print("Alice")


print("Type exit to exit")
stones()
