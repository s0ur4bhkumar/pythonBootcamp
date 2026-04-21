import random

stages = [
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
lives = 6

placeHolder = "".join(["_" for i in chosen_word])

game_over = False
correct_guesses = []
print(chosen_word)
print(placeHolder)

while not game_over and lives != 0:
    guess = input("enter your choice of letter: ").lower()
    display = ""

    for i in chosen_word:
        if i == guess:
            display += guess
            correct_guesses.append(guess)
        elif i in correct_guesses:
            display += i
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives - 1])

    if "_" not in display:
        game_over = True
        print("you win")
    if lives == 0:
        print("you lose")
