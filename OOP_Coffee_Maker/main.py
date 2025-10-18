# Import necessary classes from other modules
from menu import Menu
from Coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the money machine, coffee maker, and menu
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Boolean flag to keep the machine running
is_on = True

# Print current resources (water, milk, coffee) and money report
coffee_maker.report()
money_machine.report()

# Main loop to keep the coffee machine running
while is_on:
     # Get the available drink options as a string (e.g., "espresso/latte/cappuccino")
    options = menu.get_items()
    # Prompt user to make a selection
    choice = input("What would you like? ({options}): ")
     # If user types "off", turn the machine off
    if choice == "off":
        is_on = False
    # If user types "report", print current resource and money status
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
     # Otherwise, try to make the selected drink
    else:
         # Otherwise, try to make the selected drink
        drink = menu.find_drink(choice)

        # Check if there are enough resources and payment is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             # If both checks pass, make the coffee
              coffee_maker.make_coffee(drink)
