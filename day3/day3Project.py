print("""

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-'''-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

""")

print("welcome to treasure island. Your mission is to find the treasure")
choice = input("Hmmmm!, there is a split, where do you want to go?, left or right: ")
if choice == "right":
    print("Oh no!, a monster, RUNNNNNNNN!")
    print("womp! womp!")
    print("Better luck next time")
else:
    choice = input("Another hurdle, this time a lake, do you want to swim or wait?: ")
    if choice == "wait":
        doorChoice = input(
            "This is the last stage, choose between red, blue and yellow door: "
        )
        if not doorChoice == "yellow":
            print("KABOOOOMMMMMMMMM!")
            print("sigh!, another one gone")
        else:
            print("congratulations!, you are a millionare now")
    else:
        print("wellll, atleast the croc won't make the hungry noises tonight")
