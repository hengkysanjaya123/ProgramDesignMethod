import matplotlib.pyplot as plt


numx = list(range(1, 1001))
numy = [x**2 for x in numx]
print(numy)

# plt.scatter(numx, numy, c ='red', edgecolor = 'none', s = 80)

#create gradient color
plt.scatter(numx, numy, c = numy, cmap = plt.cm.Blues, edgecolor = 'none', s = 80)

#set the range for each axis
plt.axis([0, 1100, 0,1100000])

# plt.show()
plt.savefig("C:\\Users\\Hengky Sanjaya\\PycharmProjects\\Beginning\\Program Design Methods\\DataVisualization\\bleh.png")

