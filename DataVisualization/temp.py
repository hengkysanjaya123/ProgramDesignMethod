import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
numx = [1, 3, 5, 7, 9]
numy = [2, 4, 6, 8, 10]

plt.title("Series of numbers", fontsize = 24)
plt.title("Series of numbers", fontsize = 18)
plt.title("Series of numbers", fontsize = 14)
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")

plt.plot(squares, marker = 'o', linewidth = 5)
plt.plot(numx, numy, marker = '*')

plt.tick_params(axis ='both', labelsize = 12)

plt.legend(["Squares", "numx and numy"])


plt.show()
