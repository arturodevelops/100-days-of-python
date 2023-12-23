print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 

print('You encounter a crosroads in the forest on the way to the castle, will you go left or right?\n')
first_choice = input("left or right?: ")

if first_choice.lower() == "left":
    print("You stumble upon a river, however there seems to be a boat on its way here. Will you wait for the boat or swim across the river? \n")
    second_choice = input("swim or wait?: ")
    if second_choice.lower() == "wait":
        print("The boat was suspiciously empty. You sail the boat to the castle gates. There are three different colors: red, yellow, or blue. Which door will you take? \n")
        third_choice = input("red, blue, or yellow?: ")
        if third_choice.lower() == "yellow":
            print("You found the treasure chest. You win!")
        elif third_choice.lower() == "red":
            print("As you opened the door, flames came out of the door and burned you alive. Game over.")
        elif third_choice.lower() == "blue":
            print("You opened the door and entered the dark room the blue door revealed. Suddenly, a beast appeared out of nowhere and ate you. Game over")
        else:
            print("By not making a choice, a trapdoor opened belowed you and killed you. Game over.")
    else: 
        print("As you attempted to cross the river, a shark attacked you. Game over.")
else:
    print("You encounter a bear and it kills you. Game over")


