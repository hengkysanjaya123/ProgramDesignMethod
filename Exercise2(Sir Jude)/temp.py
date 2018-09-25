spam = "House Of Wax"

print(spam[0].isupper())
print("test".islower())
print("test".isalpha())
print(spam.istitle())
print(spam.startswith("HOuse"))
print(spam.startswith("Wax"))

print(spam.endswith("House"))
print(spam.endswith("Wax"))

list = ['a', 'b', 'c' ,'d']
x = ''
print(x.join(list))


str1 = "I am gonna be split"
print(str1.split())


# remove spaces
spam = "    Hi there    "
print(spam.strip())
print(spam.lstrip())
