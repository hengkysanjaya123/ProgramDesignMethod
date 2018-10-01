import os


myPath = os.getcwd()

# os.makedirs('Sample')


# os.makedirs("D:\\hengky\\# Kuliah\\Program Design Methods\\test")
# print(myPath)
# print(os.path.getsize(myPath))
# print(os.listdir(myPath))
#
# print(os.path.abspath(myPath))
# print(os.path.relpath(myPath))


# print(os.getcwd())
# readFile = open('hello.txt')
# print(readFile.read())

# with open(myPath + '\\hello.txt', 'r') as f:
#     contents = f.read()
#     print(contents)



#Write Statement
baconFile = open('bacon.txt','a')
baconFile.write("\nabc")
baconFile.close()

baconFile = open('bacon.txt', 'r')
print(baconFile.read())
