while True:
    try:
        n = int(input("Please input number of dimension (odd) : "))
        if(n % 2 == 0):
            print("Please input odd number")
        else:
            break
    except ValueError:
        print("Please input integer")

x = 0
y = int((n - 1) / 2)
number = 2

array = [[0 for i in range(0,n)] for i in range(0, n)]
array[x][y] = 1

while number <= n * n:
    a = (x-1+n) % n
    b = (y+1) % n

    if(array[a][b]):
        a = x+1
        b = y

    x = a
    y = b

    array[x][y] = number

    number+=1

for a in array:
    print(a)
