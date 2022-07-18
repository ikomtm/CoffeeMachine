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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0

def request():
    """"""
    request = input ("What would you like? (espresso/latte/cappuccino): ")
    if request == 'off':
        print("Machine is off")
    if request == 'report':
        reporting()
    else:
        making_choice(request)

def making_choice():
    if key == 'e' or key == 'espresso':
        choice = MENU[0]
    if key == 'l' or key == 'latte':
        ingrdnts = MENU["latte"]["ingredients"]
        cost = MENU["latte"]["cost"]
    if key == 'c' or key == 'capuccino':
        ingrdnts = MENU["cappuccino"]["ingredients"]
        cost = MENU["cappuccino"]["cost"]


def making_coffee(ingrdnts):
    for resource in resources:
        if resource in ingrdnts:
            if ingrdnts[resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}")
            else:
                resources[resource] -= ingrdnts[resource]
        else:
            continue


def reporting():
    for k in resources:
        if k == 'water' or k == 'milk':
            print(f"{k.capitalize()}: {resources[k]}ml")
        elif k == 'coffee':
            print(f"{k.capitalize()}: {resources[k]}g")
    print(f"Money: ${money}")

def insert_coins():
    total_insert = 0
    for coin in COINS:
        coin_input = int(input(f"How many {coin}?: "))
        total_insert += (coin_input*COINS[coin])
    return round(total_insert, 2)

def check_money(cost, incoins):
    if cost > incoins:
        print("Sorry that's not enough money. Money refunded.")
    elif cost < incoins:
        print(f"Here is {incoins-cost} in change ")


def check_resources():
    pass


request()
choice = making_choice()
ingrdnts = choice[0]
cost = choice[1]
print(ingrdnts)
print(cost)


