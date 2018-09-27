#declare a pascal triangle function
def pascalTriangle(num):
    #create an empty list to store the result
    array = []

    for i in range(num):
        #add an array to each row
        array.append([])
        for j in range(i + 1):
            #check if current location is first column or last column
            if(j == 0 or j == i):
                array[i].append(1)
            #else add the value from previous row from both column ( same column and 1 before)
            else:
                array[i].append(array[i-1][j] + array[i-1][j-1])
    return array

print("Type exit to exit")
while True:
    #ask user to input number of row
    num = input("Please input number of rows : ")
    #set to lower case
    num = num.lower()
    #if exit then break
    if(num == "exit"):
        break
    else:
        #validation input value
        try:
            num = int(num)
        except ValueError:
            print("Please input integer value")
            continue

        #call the function
        array = pascalTriangle(num)

        #display the result
        print("============================")
        for i in array:
            for j in i:
                print(j, end=" ")
            print()

        print("============================")
        print()
