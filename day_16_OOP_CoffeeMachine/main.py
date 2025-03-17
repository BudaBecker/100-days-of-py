from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True
while on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == "off":
        on = False
        print("Turning it off. Bye.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif choice == "refill":
        coffee_maker.refill()
        print("Machine Refilled!")
    else:
        print("Invalid command. Try again (or type 'off' to turn off).")
    print("\n")