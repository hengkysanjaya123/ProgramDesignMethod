def tower(n):
    char = 'A'
    for i in range(n):
        o = n - i - 1
        print(" "*o , end="")

        for j in range(0, i + 2):
            print(str(char), end = "")

        print("AAAAAAAAAAAAA")


tower(5)
