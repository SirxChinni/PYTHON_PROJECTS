MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def process_amount():
    print("Please insert coins")
    total = int(input("No.of rupees?: "))
    total += int(input("No.of paise?: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry! Insufficient amount entered. Amount refunded")
        return False
        # print(f"please enter an extra amount of Rs.{(drink_cost - money_received)/100}")
        # is_transaction_successful(money_received + process_amount(), drink_cost)
    elif money_received >= drink_cost:
        print("transaction successful")
        change = round(money_received-drink_cost, 2)
        print(f"Please collect a change of Rs.{change}")
        return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Enjoy your drink and have a nice day")


profit = 0
is_on = True
while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino) ")
    print(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_amount()
            if is_transaction_successful(payment, drink["cost"]):
                profit += drink["cost"]
                make_coffee(choice, drink["ingredients"])


