from data import *


def check_resources(demand_ingredient):
    for item in demand_ingredient:
        if demand_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def reduce_resources(demand_ingredient):
    for item in demand_ingredient:
        resources[item] -= demand_ingredient[item]


money_inside_machine = 0
end_program = False
while not end_program:
    print("Pshh! 🤫. You can generate report of machine using 'report' keyword. 'off' shuts down the machine")
    task = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if task == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_inside_machine}")
    elif task == "off":
        end_program = True
    else:
        drink = MENU[task]
        if not check_resources(drink["ingredients"]):
            end_program = False
        else:
            print("Please insert coins.")
            coins = 0.25 * int(input("How many quarters?: ")) + 0.10 * int(input("How manny dime?: ")) + 0.05 * int(
                input("How many nickel?: ")) + 0.01 * int(input("How many penny?: "))
            if coins < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif coins == drink["cost"]:
                print(f"Here's your {task} ☕️. Enjoy!")
                reduce_resources(drink["ingredients"])
                money_inside_machine += drink["cost"]
            else:
                print(f"Here is {round(coins - drink["cost"], 2)} in change.")
                print(f"Here's your {task} ☕️. Enjoy!")
                reduce_resources(drink["ingredients"])
                money_inside_machine += drink["cost"]
