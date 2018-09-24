def overlapping(x, y):
    for i in x:
        for j in y:
            if(i == j):
                return True
    return False

data1 = [1,2,3,4,5]
data2 = [5,6,7,8,9]
print(overlapping(data1, data2))
