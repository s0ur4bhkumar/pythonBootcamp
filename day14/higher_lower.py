import random

import game_data

vs = r"""
__     ______
\ \   / / ___|
 \ \ / /\___ \
  \ V /  ___) |
   \_/  |____/

"""


def round_check(user_input, A, B):
    if user_input == "A":
        if A["follower_count"] > B["follower_count"]:
            print("you are right")
            return True
        else:
            print("you are wrong")
            return False
    elif user_input == "B":
        if A["follower_count"] < B["follower_count"]:
            print("you are right")
            return True
        else:
            print("you are wrong")
            return False


def select_Options():
    option_A = random.choice(game_data.data)
    option_B = random.choice(game_data.data)

    while option_A == option_B:
        option_B = random.choice(game_data.data)

    return [option_A, option_B]


def round(A, B):
    print(f"compare A: {A['name']},{A['description']} from {A['country']}")

    print(vs)

    print(f"compare B: {B['name']},{B['description']} from {B['country']}")

    user_input = input('which have more followers "A" or "B": ')

    return user_input


def main():
    A, B = select_Options()
    continue_game = True
    score = 0

    while continue_game:
        updated_game_data = [i for i in game_data.data if i != A and i != B]
        user_input_options = {"A": A, "B": B}
        user_input = round(A, B)
        print("A: ", A)
        print("B: ", B)
        continue_game = round_check(user_input, A, B)
        if continue_game:
            print(user_input_options)
            A, B = user_input_options[user_input], random.choice(updated_game_data)
            score += 1
    print(f"your final score is {score}")


main()
