# use loop to validate input error
while True:
    try:
        n = int(input("Please input number of dimension (odd) : "))
        #check if input is not odd number
        if(n % 2 == 0):
            print("Please input odd number")
        else:
            break
    except ValueError:
        print("Please input integer")

#declare variable
x = 0
# set the default y positioin in first line and middle column of array
y = int((n - 1) / 2)
number = 2

#create an 2d array with default 0 value
array = [[0 for i in range(0,n)] for i in range(0, n)]

# set default position of number 1
array[x][y] = 1

#loop until n * n
while number <= n * n:
    # set a and b
    # a for go up
    # b for go right
    a = (x-1+n) % n
    b = (y+1) % n

    #check if its already filled by another number so Go Down
    if(array[a][b]):
        a = x+1
        b = y

    # set the value of a and b  to x and y
    x = a
    y = b

    # set the current number to current coordinate of array
    array[x][y] = number

    #increment the number
    number+=1

#display the result
for a in array:
    print(a)
