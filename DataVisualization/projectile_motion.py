import math
import matplotlib.pyplot as plt

velocity = int(input("Enter the initial velocity (m/s) >>"))
angle = int(input("Enter the angle of projection (degrees) >>"))
g = 9.81

vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))

listCx = []
listCy = []

t = 0
time = math.ceil(2 * vy / g)
while ( t <= time):
    cx = vx * t
    cy = (vy * t - (g/2)*t*t)

    if(cy > 0):
        listCx.append(cx)
        listCy.append(cy)

    t += 0.02

# plt.axis([0, 1000])
print(listCx)
print(listCy)

plt.title("Projectile motion of ball")

plt.plot(listCx, listCy)

plt.show()
