initial_velocity = 0
time_spent = int(input("Please input Time​ ​spent​ ​on​ ​the​ ​road​ :"))
acceleration = int(input("Please input Acceleration : "))
distance = int(input("Please input distance : "))
speed_limit = 60

v = 0
s = 0
for i in range(0, time_spent + 1):
    v = initial_velocity + acceleration * i
    s = initial_velocity * i + 1/2 * acceleration* i * i
    print("Duration: "+str(i)+ " Distance : " + "*" * int(s /10))


if (v > speed_limit):
    print("The​ ​person​ ​went​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was​ ​"+str(v)+" ​m/s)")
else:
    print("The​ ​person​ ​did​ ​not​ ​go​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was​ "+str(v)+" ​m/s) ")


if(s >= distance):
    print("The​ ​person​ ​reached​ ​the​ ​destination.​ ​(Reached​ ​"+str(s)+"m)")
else:
    print("The​ ​person​ ​did​ ​not​ ​reach​ ​the​ ​destination.​ ​(Reached​ "+str(s)+" m) ")
