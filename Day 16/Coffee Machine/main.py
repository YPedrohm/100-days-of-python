from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    menu.get_items()
    order = input("What would you like? (espresso/latte/cappuccino)").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif order == "off":
        print("Turning off...")
        break

    drink = menu.find_drink(order)
    can_make = coffee_maker.is_resource_sufficient(drink)

    if can_make:
        can_pay = money_machine.make_payment(drink)
        if can_pay:
            coffee_maker.make_coffee(drink)