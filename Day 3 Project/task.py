print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("You're at a crossroads. Do you turn left or right? Enter "
                  "'l' or 'r': ").lower()
if direction == "l":
    print("\nYou are ambushed by goblins. They kill you and take your "
          "belongings. Game over :(")
else:
    direction = input("\nYou come to a lake. Swim across or take the small "
                      "boat you see? Enter 'swim' or 'boat': ").lower()
    if direction == "swim":
        print("\nYou get half way across and become extremely tired. "
              "You have drowned. Game over :(")
    else:
        direction = input("\nYou come to three magical doors. Blue, Red, and "
                          "Yellow. Which door do you choose? Enter 'blue', "
                          "'red' or 'yellow': ").lower()
        if direction == "red":
            print("\nYou fall into a pit of lava and die. Game over :(")
        elif direction == "yellow":
            print("\nYellow is the worst color. You are flayed by a thousand "
                  "dull spoons. Game over :(")
        else:
            print("\nYou have found the treasure! Congratulations! You win!!!")
