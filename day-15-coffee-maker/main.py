from recipe import coffee_recipies


available_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


def check_for_sufficient_resources(coffee_name: str, available_resources: dict):
    """
    This method will check for sufficient resources are available for preparing given coffee_name.
    If not then will print the error message else return True and will prepare coffee.
    """
    required_resources = coffee_recipies.get(coffee_name)
    for resource in required_resources:
        if resource != 'money' and required_resources.get(resource) > available_resources.get(resource):
            print(f"Sorry there is not enough {resource.title()}.")
            return False
    return True


def process_coin():
    no_of_quarters = int(input("How many quarters? "))
    no_of_dimes = int(input("How many dimes? "))
    no_of_nickles = int(input("How many nickles? "))
    no_of_pennies = int(input("How many pennies? "))
    return (no_of_quarters * 0.25) + (no_of_dimes * 0.1) + (no_of_nickles * 0.05) + (no_of_pennies * 0.01)


def check_for_sufficient_money(coffee_name, total_amount):
    """
    Check for sufficient money is provided for given coffee_name.
    If No, refund money
    If more than required, offer change and prepare coffee.
    Update the available_resources
    """
    required_resources = coffee_recipies.get(coffee_name)
    coffee_price = required_resources.get("money")
    if coffee_price > total_amount:
        print(f"Sorry that's not enough money. Money refunded.")
    else:
        if coffee_price < total_amount:
            change_to_offer = total_amount - coffee_price
            print(f"Here is ${change_to_offer:.2f} dollars in change.")
        print(f"Thanks for order!!. Here is your {coffee_name}")

        # Update resources.
        for item in required_resources:
            if item != 'money':
                available_resources[item] -= required_resources.get(item)
            else:
                available_resources[item] += required_resources.get(item)


def print_report(available_resources: dict):
    """
    This will print the available resources report
    """
    for key, value in available_resources.items():
        if key in ['water', 'milk']:
            print(f"{key.title()}: {value}ml")
        elif key == 'coffee':
            print(f"{key.title()}: {value}g")
        else:
            print(f"{key.title()}: ${value}")


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice.lower() == 'report':
        print_report(available_resources)
    elif user_choice.lower() in coffee_recipies:
        coffee = coffee_recipies.get(user_choice.lower())
        is_res_aval = check_for_sufficient_resources(
            user_choice.lower(), available_resources)
        if is_res_aval:
            print(f"{user_choice.title()} costs ${coffee.get('money')}")
            total_money = process_coin()
            check_for_sufficient_money(user_choice, total_money)
    elif user_choice.lower() == 'off':
        print("Turning off machine!!")
        break
