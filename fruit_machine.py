import random
import sys

fruits = ("Cherry", "Bell", "Lemon", "Orange", "Star", "Skull")
money = 1.00
count = 0

def play(money):

    result = []

    if money >= 0.20:
        print(f"You have £{money}")
        affirm = input("Would you like to play a round on the Fruit Machine? Y/N: ")

        if affirm == "Y" or affirm == "y":
            result.clear()
            money -= 0.20

            for i in range(1, 3):
                count = random.randint(1, 5)

                if count == 1:
                    result.append("Cherry")
                elif count == 2:
                    result.append("Bell")
                elif count == 3:
                    result.append("Lemon")
                elif count == 4:
                    result.append("Orange")
                elif count == 5:
                    result.append("Star")
                elif count == 6:
                    result.append("Skull")

                output1 = result.count("Cherry")
                output2 = result.count("Bell")
                output3 = result.count("Lemon")
                output4 = result.count("Orange")
                output5 = result.count("Star")
                output6 = result.count("Skull")

                if output1 == 2:
                    money += 0.50
                elif output2 == 2:
                    money += 0.50
                elif output3 == 2:
                    money += 0.50
                elif output4 == 2:
                    money += 0.50
                elif output5 == 2:
                    money += 0.50
                elif output6 == 2:
                    money -= 1.00

                elif output1 == 3:
                    money += 1.00
                elif output2 == 3:
                    money += 5.00
                elif output3 == 3:
                    money += 1.00
                elif output4 == 3:
                    money += 1.00
                elif output5 == 3:
                    money += 1.00
                elif output6 == 3:
                    money -= money

        elif affirm == "N" or affirm == "n":
            print("Thanks for playing!")
            sys.exit()

    elif money < 0.20:
           print("You have run out of money, time to get a new habit. Or an intervention. Depends")


play(money)
