import random

mode = {"easy": 10, "hard": 5}
number = random.randint(1, 101)


def main():
    user_mode = input("select mode 'easy' or 'hard' : ")
    while mode[user_mode] > 0:
        print(f"you have {mode[user_mode]} tries to guess the number")
        guess = int(input("Guess the number: "))
        if guess > number:
            print("Too high, guess again")
            mode[user_mode] -= 1
        elif guess < number:
            print("Too low, guess again")
            mode[user_mode] -= 1
        else:
            print("you won")
            break


main()
