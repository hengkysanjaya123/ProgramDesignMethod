import matplotlib.pyplot as plt
import math

g = 9.81
nCase = int(input("How many trajectories?"))
listVelocity = []
for i in range(nCase):
    velocity = int(input("Enter the initial velocity for trajectory "+str(i+1)+" (m/s) :"))
    angle = int(input("Enter the angle of projection for trajectory 1 (degress) :"))

    listVelocity.append(velocity)

    vx = velocity * math.cos(math.radians(angle))
    vy = velocity * math.sin(math.radians(angle))

    time = math.ceil(2 * vy / g)

    listCx = []
    listCy = []

    t = 0
    while(t < time):
        cx = vx*t
        cy = (vy*t - (g/2)*t*t)

        if(cx > 0 and cy > 0):
            listCx.append(cx)
            listCy.append(cy)

        t +=0.02

    plt.plot(listCx, listCy)

plt.legend(listVelocity)
plt.show()
