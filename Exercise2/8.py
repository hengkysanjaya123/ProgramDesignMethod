#8.	Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******


#declare function
def histogram(listData):
    #loop each element in listData
    for i in listData:
        # print star times the value of i
        print('*' * i)

#calling function
histogram([4, 9, 7])
