import random as random

li = []

#player coordinates
playerX = 0
playerY = 0

#read file
file = open("poke.txt", "r")
content = file.read().split("\n")
for row in range(0,8):
    f = content[row].split(",")
    li.append([])
    for col in range(len(f)):
        if f[col] == "0":
            print("o", end="  ")
            li[row].append("o")
        elif f[col] == "1":
            print("X", end="  ")
            li[row].append("o")
            #saving player coordinates
            playerX = col
            playerY = row
        elif f[col] == "2":
            print("#", end="  ")
            li[row].append("#")
    print(" ")

#last loc, ground,0, or grass,2
if content[8] == "0":
    li[playerY][playerX] = "o"
elif content[8] == "2":
    li[playerY][playerX] = "#"

file.close()

print('''
welcome to poke game:)
==================
       MENU
==================
[1] Move up
[2] Move down
[3] Move left
[4] Move right
[5] Save and exit
-------enJOY------
''')

#poke encounter chance
def poke():
    chance = random.randint(0,5)
    if chance == 0:
        print('''~~~There is a pokemon. (^;^)
        ''')

while True:
    inp = int(input("Your choice: "))
    if inp == 1:
        if (playerY - 1 >= 0):
            playerY -= 1
    elif inp == 2:
        if (playerY + 1 <= 7):
            playerY += 1
    elif inp == 3:
        if (playerX - 1 >= 0):
            playerX -= 1
    elif inp == 4:
        if (playerX + 1 <= 7):
            playerX += 1
    elif inp == 5:
        file = open("poke.txt", "w")
        text = ""
        for i in range(len(li)):
            for j in range(len(li[i])):
                if i == playerY and j == playerX:
                    text += "1"
                elif li[i][j] == "o":
                    text += "0"
                elif li[i][j] == "#":
                    text += "2"

                if j < len(li[i]) - 1:
                    text += ","
            text += "\n"
#9th line in poke.txt
        if li[playerY][playerX] == "#":
            text += "2"
        else:
            text += "0"

        file.write(text)
        file.close
        break
#poke chance
    if (li[playerY][playerX] == "#"):
        poke()
#player current loc
    for i in range(len(li)):
        for j in range(len(li[i])):
            if i == playerY and j == playerX:
                print("X", end="  ")
            elif li[i][j] == "o":
                print("o", end="  ")
            elif li[i][j] == "#":
                print("#", end="  ")
        print(" ")
