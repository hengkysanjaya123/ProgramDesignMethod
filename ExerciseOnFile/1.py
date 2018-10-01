"""
1. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in
either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes.
Make sure your program ignores capitalization.
"""

import os
import string

def replaceWord(stringValue):
    dataPunctuation = string.punctuation

    for i in dataPunctuation:
        stringValue = stringValue.replace(i, '')

    return stringValue

def hapax(filename):
    filename = filename.lower()

    readFile = open(os.getcwd() + '\\'+filename, 'r')
    data = readFile.read().lower()
    data = data.split()

    listOccurs = {}
    for i in data:
        current = replaceWord(i)
        listOccurs.setdefault(current, 0)
        listOccurs[current] = listOccurs[current] + 1

    print("Total Words : " + str(len(listOccurs)))
    print("--------------------------------------------------------------------------------")
    print("Hapax word : ")
    print("--------------------------------------------------------------------------------")
    for i in listOccurs.keys():
        nOccurs = listOccurs.get(i)
        if(nOccurs == 1):
            print(i , end=",")

    print()
    print("Most common : ")
    print("--------------------------------------------------------------------------------")
    maximum = max(listOccurs, key=listOccurs.get)
    print(maximum, listOccurs[maximum])

hapax("books.txt")
