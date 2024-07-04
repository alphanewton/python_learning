from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_finished = False

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

while not is_finished:
    action = input("What would you like? (espresso/latte/cappuccino/):")

    if action == "off":
        is_finished = True
    elif action == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

