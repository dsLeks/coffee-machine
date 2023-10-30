from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


print("Here is the Menu: ")
menu = Menu()
print(menu.get_items())
usr_input = input("What would you like to order?: ").lower()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while(usr_input != "off"):
    if usr_input == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(usr_input)
        if drink != None:
            cm_resources = coffeeMaker.is_resource_sufficient(drink)
            if cm_resources != None:
                if drink != None and moneyMachine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)
        
            
    usr_input = input("What would you like? (espresso/latte/cappuccino): ")
