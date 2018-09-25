# 1.	Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.


#define function
def max_of_three(x,y,z):
    #create an array contains of x, y, z
    array = [x,y,z]
    #sort array ascendingly
    array.sort()
    #return the last element of array
    return array[len(array)-1]

#calling function
print("The largest : "+ str(max_of_three(9, 5, 11)))
