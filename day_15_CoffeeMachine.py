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
        "cost": 2.5
        },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            },
        "cost": 3.0
        },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(drink: str) -> bool:
    ingredients_missing = []
    for ingredients in MENU[drink]["ingredients"]:
        if resources[ingredients] < MENU[drink]["ingredients"][ingredients]:
            ingredients_missing.append(ingredients)
    
    if len(ingredients_missing) == 0:
        return True
    else:
        print(f"Sorry there is not enough {ingredients_missing}")
        return False
        

def payment(drink: str) -> bool:
    coins = {
        "quarters": 0.25, 
        "dimes": 0.10, 
        "nickles": 0.05, 
        "pennies": 0.01
        }
    money_paid = 0
    print(f"Please insert coins. (${MENU[drink]["cost"]})")
    for coin_keys in coins:
        money_paid += round(int(input(f"How many {coin_keys} (${coins[coin_keys]})?: ")) * coins[coin_keys], 2)
    if money_paid == MENU[drink]["cost"]:
        print("Exact price, no change needed!")
        return True
    elif money_paid > MENU[drink]["cost"]:
        print(f"Here is ${money_paid-MENU[drink]["cost"]} in change.")
        return True
    else:
        print("Sorry that's not enought money. Money refunded.")
        return False
    

def change_resources(drink: str) -> dict:
    changed_resources = resources.copy()
    for ingredients in MENU[drink]["ingredients"]:
        changed_resources[ingredients] = resources[ingredients] - MENU[drink]["ingredients"][ingredients]
    changed_resources["money"] = resources["money"] + MENU[drink]["cost"]
    return changed_resources

on = True
while (on):
    promt_user = input("What would you like? (espresso/latte/cappuccino): ")
    if promt_user in MENU.keys():
        if check_resources(promt_user):
            if payment(promt_user):
                print(f"Here is your {promt_user} ☕. Enjoy!")
                resources = change_resources(promt_user)

    
    elif promt_user == "off":
        on = False
        print("Turning it off. Bye.")
    
    elif promt_user == "report":
        print("\nResources:")
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")

    elif promt_user == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Machine Refilled!")
    
    else:
        print("Invalid command. Try again (or type 'off' to turn off).")
    print("\n")