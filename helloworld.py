import sys
import random
exitChoice = "someValue"
while exitChoice != "exit":
    try:
        age = int(input("what is your age?"))
        randomAge = age + random.randint(1, 10)
        newAge = 0
        listOfAges = [0]
        if age == 20 or age == 30 or age == 40:
            print("nice age!")
        elif age <= 18:
            print("so young! get out of here")
        elif age >= 100:
            print("you cant be that old!! you sure your not younger ;)?")
        else:
            for i in range(0, 10):
                newAge = age + i
                print("your age in", i, " years will be ", newAge)
                listOfAges.append(newAge)
            del listOfAges[0]
            print("and this is the list of ages:", listOfAges, "in five years you will be", listOfAges[5])
            print("I have also randomized your age. you are now", str(randomAge))
        exitChoice = input("press enter to try again or exit to exit")

    except Exception as e:
        print(e)
