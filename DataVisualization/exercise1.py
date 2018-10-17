import matplotlib.pyplot as plt

first_five = []
for i in range(1, 5+1):
    first_five.append(i ** 3)

first_fivethousand = []
for i in range(1, 5000 + 1):
    first_fivethousand.append(i ** 3)

plt.plot(first_five, marker = 'o', linewidth = 2)
plt.plot(first_fivethousand, marker = '*', linewidth = 2)
# plt.scatter(first_five, first_fivethousand, c = first_fivethousand, cmap = plt.cm.Blues, edgecolor = 'none', s = 80)
plt.show()
