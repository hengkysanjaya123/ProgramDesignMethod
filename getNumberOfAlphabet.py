n = 20
data = ""
for i in range(1, n + 1):
    data += str(i)

for i in range(0, 10):
    print(str(i) + " : " + str(data.count(str(i))))