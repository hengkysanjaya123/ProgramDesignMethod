#6.	Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

#declare function
def overlapping(x, y):
    #loop element in x
    for i in x:
        #loop element in y
        for j in y:
            #check if element in x equals to element in y
            if(i == j):
                return True
    return False

#calling function
data1 = [1,2,3,4,5]
data2 = [5,6,7,8,9]
print(overlapping(data1, data2))
