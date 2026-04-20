import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissor]

player = int(
    input(
        "what do you want to choose? choose 0 for rock, 1 for paper, or 2 for scissors: "
    )
)

player_win_combinations = [
    [rock, scissor],
    [paper, rock],
    [scissor, paper],
]

draw_combinations = [[rock, rock], [paper, paper], [scissor, scissor]]

player_choice = choices[player]
computer_choice = random.choice(choices)

print("player")
print(player_choice)

print("computer")
print(computer_choice)

result = [player_choice, computer_choice]

if result in player_win_combinations:
    print("you won")
elif result in draw_combinations:
    print("it's a draw")
else:
    print("computer won")
