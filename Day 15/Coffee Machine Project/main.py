import sys

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_choice(choice):
    if choice == "off":
        print("turning off the coffee machine...")
        sys.exit()
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
        return False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        working = True
        for ingredient in MENU[choice]["ingredients"]:
            needed = MENU[choice]["ingredients"][ingredient]
            available = resources[ingredient]
            if available < needed:
                print(f"Sorry, you can't {choice}! Ingredients are missing.")
                working = False
        return working
    else:
        print("Please choose a valid option.")
        return False

def payment(choice):
    price = MENU[choice]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    result = total - price
    if result < 0:
        print(f"Sorry that's not enough money. Money refunded.")
        payment_made = False
        return payment_made
    if result >= 0:
        resources["money"] += MENU[choice]["cost"]
        print(f"Here is ${result:.2f} in change")
        payment_made = True
        return payment_made

def deduct_ingredient(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]

while True:
    choice = input("What would you like? (Espresso/Latte/Cappuccino) ").lower()
    working = check_choice(choice)
    if working:
        payment_made = payment(choice)
        if payment_made:
            deduct_ingredient(choice)
            print(f"Here is your {choice} ️☕️. Enjoy!")