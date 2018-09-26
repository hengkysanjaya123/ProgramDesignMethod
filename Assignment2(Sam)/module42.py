
def modulo():
    dict = {}
    for i in range(10):
        number = int(input("Please input a number : "))
        mod = number % 42
        dict.setdefault(mod, 0)
        dict[mod] = dict[mod] + 1
    return len(dict)


print(modulo())

