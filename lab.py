x = 0
y = int(input("Input another number:"))
while x < y:
    x += 1
    print(" " * (y-x) + "*" * x)


#inp = int(input("insert a number: "))

#for i in range(1, inp):
#    print("*" * inp)

x =0
y = int(input("Input a number:"))
while x < y:
    x += 1
    print("*" * x)
    if x == y:
        break

x = 0
y = int(input("Input another number:"))
while x < y:
    x += 1
    print(" " * (y-x) + "*" * x)

x =0
y = int(input("Input a number:"))
while x < y:
    y -= 1
    print("*" * (y+1))
    if x == y:
        break

x = 0
y = int(input("Input a number:"))
while x < y:
    x += 1
    print(" " * x + "*" * (y-x+1))

x = 0
y = int(input("Input another number:"))
while x < y:
    x += 1
    print(" " * (y-x) + "*" * x + "*" * (x-1) + " " * (y-x+1))

x = 0
y = int(input("Input another number:"))
z = 0
while x < y:
    x += 1
    print(" " * (y-x) + "*" * x + "*" * (x-1))
    while x == y:
        z += 1
        print(" " * z + "*" * (y-z) + "*" * (y-z-1))
        if z == y:
            break
