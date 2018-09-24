def max_of_three(x,y,z):
    array = [x,y,z]
    array.sort()
    return array[len(array)-1]

print("The largest : "+ str(max_of_three(9, 5, 11)))
