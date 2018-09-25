#5.	Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)

#declare function
def is_member(x,a):
    #loop element in a
    for i in a:
        #check if x equals to each element of a
        if(x == i):
            #return true if x == i
            return True

    #else return false
    return False

#calling function
print(is_member(1, ["abc", "test2", 1]))
