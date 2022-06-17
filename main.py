print("welcome to thresure island your mission is to find the TRESSURE")
a = input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n')
lf = a.lower()
if a == "left":
    b = input(
        'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across \n')
    ws = b.lower()
    if ws == "wait":
        c = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose\n")
        ryb = c.lower()
        if ryb == "red":
            print("It's a room full of fire. Game Over")
        elif ryb == "yellow":
            print("It's a room full of fire. Game Over")
        elif ryb == "blue":
            print("You found the treasure! You Win!")
    else:
        print("GAME OVER")


else:
    print("GAME OVER")


