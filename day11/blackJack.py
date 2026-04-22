import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score(cards):
    total = 0
    for i in cards:
        total += i
    return total


def card_initialize():
    return [random.choice(cards), random.choice(cards)]


def main():
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player_cards = card_initialize()
    computer_cards = card_initialize()
    while continue_game != "n":
        print(f"your cards: {player_cards}, current score: {score(player_cards)}")
        print(f"computer's first hand: {computer_cards[0]}")
        get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_or_pass == "n":
            computer_cards.append(random.choice(cards))
            print(
                f"your final hand: {player_cards}, final score: {score(player_cards)}"
            )
            print(
                f"computer final hand: {computer_cards}, final score: {score(computer_cards)}"
            )
            if score(player_cards) < score(computer_cards) < 21:
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
                continue

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
            get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")


main()
