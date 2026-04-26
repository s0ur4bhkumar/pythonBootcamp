from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def choice():
    choice = input("select from menu latte/espresso/cappuccino: ")
    if choice == "report":
        print("coffee machine report: ", coffee_maker.report())
        print("money machine report: ", money_machine.report())
        return
    return menu.find_drink(choice)


def main():
    coffee = choice()

    while coffee is not None:
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
                coffee = choice()
            else:
                print("payment failed")
                break
        else:
            print("not enough resources for your order")
            break


main()
