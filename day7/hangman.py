import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


placeHolder = "".join(["_" for i in chosen_word])

display = ""

print(chosen_word)
print(placeHolder)

guess = input("enter your choice of letter: ").lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display += guess
    else:
        display += "_"

print(display)
