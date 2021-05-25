from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create a new variable money_machine that will hold an oject from the MoenyMachine class
# the object is constructed when we add the parentheses
money_machine = MoneyMachine()
# similarly with cofee maker, we're constructorign a new object from class CoffeeMaker
coffee_maker = CoffeeMaker()
# constructor menu object from Menu class
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # this prints outs the report of coffee
        coffee_maker.report()
        # this prints out the current amount of money in the machine
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
