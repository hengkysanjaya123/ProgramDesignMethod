#3.	Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

#define function
def isVowel(x):
    #declare an array contains vowel character
    vowel = ['a', 'i', 'u', 'e','o']
    #return boolean value if x in array
    return x.lower() in vowel

#call function
print(isVowel('o'))
print(isVowel('j'))
