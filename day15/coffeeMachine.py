from functools import total_ordering

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(resources)


def process_coins(penny=0, nickel=0, dime=0, quarter=0):
    total = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny
    return total


def check_transaction(name, penny=0, nickel=0, dime=0, quarter=0):
    total = process_coins(penny, nickel, dime, quarter)

    if total > MENU[name]["cost"]:
        return True
    elif total == MENU[name]["cost"]:
        return True
    else:
        return False


def check_resouces(name):
    for key in resources:
        for i in MENU[name]["ingredients"]:
            if key == i:
                return resources[key] >= MENU[name]["ingredients"][i]


def manage_resources(name):
    global resources

    for key in resources:
        for i in MENU[name]["ingredients"]:
            if i == key:
                resources[key] -= MENU[name]["ingredients"][i]


def main():
    user_input = input("what would you like? (espresso/latte/cappuccino): ")

    while user_input != "off":
        if user_input == "report":
            report()
            user_input = input("what would you like? (espresso/latte/cappuccino): ")
        if check_resouces(user_input):
            print("please insert coins.")
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dime? "))
            nickel = int(input("How many nickel? "))
            pennies = int(input("How many pennies? "))

            if check_transaction(user_input, pennies, nickel, dime, quarter):
                total = process_coins(pennies, nickel, dime, quarter)
                if type(total) is float:
                    print(
                        "here is the change", round(total - MENU[user_input]["cost"], 2)
                    )
                manage_resources(user_input)
                print(f"here is your {user_input}, enjoy")
            else:
                print("not enough money, money refunded")
        else:
            print("Sorry,not enough resources for your order")

        user_input = input("what would you like? (espresso/latte/cappuccino): ")


main()
