from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

should_turn_off = False

while not should_turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        should_turn_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice.lower())
        is_res_aval = coffee_maker.is_resource_sufficient(order)
        if is_res_aval:
            payment_success = money_machine.make_payment(order.cost)
            if payment_success:
                coffee_maker.make_coffee(order)
        else:
            should_turn_off = True



