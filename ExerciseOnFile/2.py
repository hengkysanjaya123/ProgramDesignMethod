"""
2. Write a program that given a text file will create a new text file in which all the lines
from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""
import os

def createNewFile(filename):
    newPath = os.getcwd() + "\\newFile.txt"
    filename = filename.lower()
    readFile = open(os.getcwd() + "\\" + filename, 'r')

    newFile = open(newPath, 'w')

    n = 1
    for i in readFile:
        newFile.write(str(n) + ". " + i)
        n = n + 1

    readFile.close()
    newFile.close()
    print("New File Created\n" + "Location : "+newPath)

createNewFile("originalFile.txt")

