MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")

def resource_check(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("There is not enough water")
        return False
    elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
        print("There is not enough milk")
        return False
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("There is not enough coffee")
        return False
    else:
        return True

def coin_process(coffee):

    global resources

    quarters = int(input("How many quarters($0.25)?: ")) * 0.25
    dimes = int(input("How many dimes($0.1)?: ")) * 0.1
    nickles = int(input("How many nickles($0.05)?: ")) * 0.05
    pennies = int(input("How many pennies($0.01)?: ")) * 0.01
    value = round(quarters+dimes+nickles+pennies,2)

    if value >= MENU[coffee]['cost']:
        resources['money']+=MENU[coffee]['cost']
        print(f"\nHere is ${value-MENU[coffee]['cost']} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

answer=""


while answer != "off":
    answer=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "report":
        report()
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if resource_check(answer) and coin_process(answer):
            resources['water']-=MENU[answer]['ingredients']['water']
            resources['milk']-=MENU[answer]['ingredients']['milk']
            resources['coffee']-=MENU[answer]['ingredients']['coffee']
            print(f"Here is your {answer}. Enjoy!\n")
            


