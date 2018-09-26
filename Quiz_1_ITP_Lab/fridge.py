fridge = [[], [], []]
maxnum = [15, 15, 15]  # max nums in each sections

print("Welcome to our fridge, Please select number from the option:")
option = input("1. Put in fridge\n2. Take out from fridge\n3. Look at fridge\n4. Stop\nChoose a number from 1 to 4: ")
while (option != "1" and option != "2" and option != "3" and option != "4"):
    print("Invalid input")
    option = input("1. Put in fridge\n2. Take out from fridge\n3. Look at fridge\n4. Stop\nChoose a number from 1 to 4: ")

while option != "4":

    if option == "1":
        section = input("Enter section to put food in (1 or 2 or 3) : ")
        while (section != "1" and section != "2" and section != "3"):
            print("Invalid input")
            section = input("Enter section to put food in (1 or 2 or 3) : ")
        section = int(section)

        amount = input("Enter amount of food to put in : ")

        while not(amount.isdigit()):
         amount = input("Enter amount of food to put in : ")

        amount = int(amount)

        if len(fridge[section - 1]) + amount <= maxnum[section - 1]:
            food = input("Enter food name: ")
            for i in range(amount):
                fridge[section - 1].append(food)
            print(food + " is now in the fridge on section #" + str(section))
        else:
            print("Section #" + str(section) + " is full")



    if option == "2":
        section = input("Enter section to take food from (1 or 2 or 3) : ")
        while (section != "1" and section != "2" and section != "3"):
            print("Invalid input")
            section = input("Enter section to take food from (1 or 2 or 3) : ")
        section = int(section)

        food = input("Enter food name: ")
        amount = (input("Enter amount of food to remove: "))
        while not(amount.isdigit()):
         amount = input("Enter amount of food to remove : ")

        amount = int(amount)
        num = 0
        while food in fridge[section - 1] and num < amount:
            fridge[section - 1].remove(food)
            num += 1
        if num != amount:
            print("Sorry, only " + str(num) + " item(s) available and removed.")
        else:
            print(str(num) + " " + food + " removed from section #" + str(section))

    elif option == "3":
        for elements in fridge:
            print(elements)


    option = input("1. Put in fridge\n2. Take out from fridge\n3. Look at fridge\n4. Stop\nChoose a number from 1 to 4: ")
    while (option != "1" and option != "2" and option != "3" and option != "4"):
        print("Invalid input")
        option = input("1. Put in fridge\n2. Take out from fridge\n3. Look at fridge\n4. Stop\nChoose a number from 1 to 4: ")
