import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


def score(cards):
    total = 0
    for i in cards:
        if i == 11:
            if total + i > 21:
                i = 1
        total += i
    return total


def card_initialize():
    return [random.choice(cards), random.choice(cards)]


def main():
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continue_game == "n":
        return
    print(logo)
    player_cards = card_initialize()
    computer_cards = card_initialize()
    print(f"your cards: {player_cards}, current score: {score(player_cards)}")
    print(f"computer's first hand: {computer_cards[0]}")
    get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
    while continue_game != "n":
        if get_or_pass == "n":
            if score(computer_cards) == 21:
                print("you lose")
                main()
                break
            computer_cards.append(random.choice(cards))
            print(
                f"your final hand: {player_cards}, final score: {score(player_cards)}"
            )
            print(
                f"computer final hand: {computer_cards}, final score: {score(computer_cards)}"
            )
            if score(player_cards) < score(computer_cards) <= 21:
                print("you lose")
                main()
                break
            elif score(computer_cards) < score(player_cards) <= 21:
                print("you won")
                main()
                break
            elif score(computer_cards) > 21:
                print("you won")
                main()
                break
            elif score(player_cards) > 21:
                print("you lose")
                main()
                break
            else:
                print("it's a draw")

        else:
            player_cards.append(random.choice(cards))
            print(
                f"your final hand: {player_cards}, final score: {score(player_cards)}"
            )
            print(
                f"computer final hand: {computer_cards}, final score: {score(computer_cards)}"
            )
            if score(player_cards) > 21:
                print("you lose")
                main()
                break
            elif score(player_cards) == 21:
                print("you won")
                main()
                break
            get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")


main()
