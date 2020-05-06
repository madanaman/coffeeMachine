# Write your code here

current_amount = 550
current_water = 400
current_milk = 540
current_coffee = 120
current_cup_cnt = 9


def print_state():
    print("The coffee machine has:")
    print(current_water, "of water")
    print(current_milk, "of milk")
    print(current_coffee, "of coffee beans")
    print(current_cup_cnt, "of disposable cups")
    print(current_amount, "of money \n")


print_state()
action_taken = input("Write action (buy, fill, take):")
if action_taken == "buy":
    coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if coffee_type == 1:
        current_water = current_water - 250
        current_coffee = current_coffee - 16
        current_amount = current_amount + 4
        current_cup_cnt = current_cup_cnt - 1 
    elif coffee_type == 2:
        current_water = current_water - 350
        current_coffee = current_coffee - 20
        current_amount = current_amount + 7
        current_milk = current_milk - 75
        current_cup_cnt = current_cup_cnt - 1 

    elif coffee_type == 3:
        current_water = current_water - 200
        current_coffee = current_coffee - 12
        current_amount = current_amount + 6
        current_milk = current_milk - 100
        current_cup_cnt = current_cup_cnt - 1 
    print_state()
elif action_taken == "fill":
    current_water = current_water + int(input("Write how many ml of water do you want to add:"))
    current_milk = current_milk + int(input("Write how many ml of milk do you want to add:"))
    current_coffee = current_coffee + int(input("Write how many grams of coffee beans do you want to add:"))
    current_cup_cnt = current_cup_cnt + int(input("Write how many disposable cups of coffee do you want to add:"))
    print_state()
elif action_taken == "take":
    print("I gave you $", current_amount)
    current_amount = 0
    print_state()
