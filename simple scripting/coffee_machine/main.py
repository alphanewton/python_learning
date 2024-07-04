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
}

money = 0.0
is_finished = False

while not is_finished:
    action = input("What would you like? (espresso/latte/cappuccino): ")

    if action == "off":
        is_finished = True

    elif action == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}mg")
        print(f"Money : ${money}")

    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        credit = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if credit < MENU[action]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue

        end = False

        for item in MENU[action]["ingredients"]:
            if MENU[action]["ingredients"][item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                end = False
                break
            else:
                resources[item] -= MENU[action]["ingredients"][item]
                end = True

        if end:
            print(f"{action.title()} is freshly prepared.")
            money += MENU[action]['cost']
            if credit >= MENU[action]['cost']:
                print(f"Here is ${round(credit - MENU[action]['cost'],2)} dollars in change.")
