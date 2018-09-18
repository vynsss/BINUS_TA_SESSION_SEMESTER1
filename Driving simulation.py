initialv = 0
time = int(input("Time spent on road:"))
accel = int(input("Acceleration:"))
Dist = int(input("Distance travelled:"))
Speed_limit = 60

speed = accel/ time
speed = int(speed)
duration = 0

while duration <= time:
    duration += 1
    speed += accel
    d = int(speed * duration/10)
    print("Duration:",duration,"Distance:","*" * d)
    if duration == 10:
        break

if speed > Speed_limit:
    print("The person went over the speed limit.")
else:
    print("The person did not go over the speed limit.")

distance = int(speed * duration)
if distance == Dist:
    print("The person reached the destination.")
else:
    print("The person did not reach the destination.")
