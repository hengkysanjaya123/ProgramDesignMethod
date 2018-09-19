n = 3
x = 0
y = int((n - 1) / 2)
number = 2

array = []

for i in range(0, n):
    array.append([])
    for j in range(0, n):
        array[i].append(0)

array[x][y] = 1

while number <= n * n:
    a = x-1
    b = y+1

    # x = 0, y = 1
    # a= -1, b = 2
    if(a < 0):
        a = x-1+n

    if(b >= 3):
        b = y+1-n

    if(array[a][b] != 0):
        a = x+1
        b = y

    x = a
    y = b

    array[x][y] = number

    number+=1

# print result
# for i in range(0, n):
#     print(array[i])

for a in array:
    print(a)
