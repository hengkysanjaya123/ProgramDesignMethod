#11.	A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence
# to see if it is a pangram or not.

def isPangram(stringValue):
    #declare a list of a - z
    data = list("abcdefghijklmnopqrstuvwxyz")
    #create an array length of 26 with 0 default value
    array = [0 for i in range(0, len(data))]

    #loop chracter in stringValue
    for i in stringValue.lower():
        #using try catch if the i value doesnt exist in list and continue to next interation
        try:
            #get the index from list data
            idx = data.index(i)
            #increment the value
            array[idx] = array[idx] + 1
        except ValueError:
            continue

    #loop and check if there is alphabet with counter = 0
    for i in array:
        if(i == 0):
            return False

    return True


#calling
print(isPangram("The quick brown fox jumps over the lazy dogs 1"))




