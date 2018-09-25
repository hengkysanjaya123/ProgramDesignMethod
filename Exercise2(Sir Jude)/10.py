#10.	Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

#declare function
def find_longest_word(listWord):
    #declare max variable
    max = 0
    #loop each element in listWord
    for i in listWord:
        #check if length of i is greater than max value
        if(len(i) > max):
            max = len(i)

    return max


#calling
print(find_longest_word(["test", "abc", ""]))
