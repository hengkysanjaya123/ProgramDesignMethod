"""
3. Write a program that will calculate the average word length of a text stored in a file
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
"""

import os

def getAverageWord(filename):
    readFile = open(os.getcwd() + "\\" + filename, 'r')
    data = readFile.read().split()

    numberOfWord = len(data)
    totalWordLength = len(''.join(data))

    return totalWordLength / numberOfWord


print("Average word length is "+str(getAverageWord("books.txt")))

