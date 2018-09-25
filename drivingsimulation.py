#import library matplotlib to create graph
import matplotlib.pyplot as plt
#import colors library to get the list of colors
from matplotlib import colors as mcolors
#import random library to use random function
import random as rand

"""
this one i take from 
https://matplotlib.org/2.0.2/examples/color/named_colors.html
to get the list of colors
"""
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

#declare variable
distances = []
durations = []
while True:
    # do input and validate the input value
    try:
        time_spent = int(input("Please input Time​ ​spent​ ​on​ ​the​ ​road​ :"))
    except ValueError:
        print("Warning : Please input time spent correct format ( number )")
        continue

    try:
        acceleration = int(input("Please input Acceleration : "))
    except ValueError:
        print("Warning : Please input acceleration correct format ( number )")
        continue

    try:
        distance = int(input("Please input distance : "))
    except ValueError:
        print("Warning : Please input distance correct format ( number )")
        continue

    #declare variable
    initial_velocity = 0
    speed_limit = 60

    v = 0
    s = 0


    listDistance = []
    listDuration = []
    #loop for each duration
    for i in range(0, time_spent + 1):
        #count the distance
        v = initial_velocity + acceleration * i
        s = initial_velocity * i + 1/2 * acceleration* i * i
        print("Duration: "+str(i)+ " Distance : " + "*" * int(s /10))
        # add the distance and duration to list
        listDistance.append(s)
        listDuration.append(i)

    #store listdistance and listduration to list ( to view several simulation in graph )
    distances.append(listDistance)
    durations.append(listDuration)

    #check condition if over speed
    if (v > speed_limit):
        print("The​ ​person​ ​went​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was​ ​"+str(v)+" ​m/s)")
    else:
        print("The​ ​person​ ​did​ ​not​ ​go​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was​ "+str(v)+" ​m/s) ")

    #check if reached destination
    if(s >= distance):
        print("The​ ​person​ ​reached​ ​the​ ​destination.​ ​(Reached​ ​"+str(s)+"m)")
    else:
        print("The​ ​person​ ​did​ ​not​ ​reach​ ​the​ ​destination.​ ​(Reached​ "+str(s)+" m) ")

    # ask user to add more simulation data or show graph
    operation = input("Add one more data or show graph (add/show) ?")
    operation = operation.lower()

    if(operation == "add"):
        continue
    elif(operation == "show"):
        # print(listDistance)
        # print(listDuration)

        #set the background color of graph
        plt.style.use('dark_background')
        #set the x and y label of graph
        plt.ylabel("Distance")
        plt.xlabel("Duration")

        #loop for each simulation listdistance to set the plot
        for i in range(0, len(distances)):
            #set the plot data, marker ( every point ), and the random color
            plt.plot(distances[i], label = "Simulation "+ str(i + 1), ** {'marker' : 'x'}, color = colors[sorted_names[rand.randint(0, len(sorted_names))]])

        #set the title of graph
        plt.title("Driving Simulation", color = 'C0')

        #show the legend
        plt.legend()
        #show the graph
        plt.show()

    break
