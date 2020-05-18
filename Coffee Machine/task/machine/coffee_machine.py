# Write your code here
class Coffee:
    def __init__(self):
        self.current_amount = 550
        self.current_water = 400
        self.current_milk = 540
        self.current_coffee = 120
        self.current_cup_cnt = 9
        self.perform_action()

    def print_state(self):
        print("The coffee machine has:")
        print(self.current_water, "of water")
        print(self.current_milk, "of milk")
        print(self.current_coffee, "of coffee beans")
        print(self.current_cup_cnt, "of disposable cups")
        print(self.current_amount, "of money \n")

    def perform_fill(self):
        self.current_water = self.current_water + int(input("Write how many ml of water do you want to add:"))
        self.current_milk = self.current_milk + int(input("Write how many ml of milk do you want to add:"))
        self.current_coffee = self.current_coffee + int(
            input("Write how many grams of coffee beans do you want to add:"))
        self.current_cup_cnt = self.current_cup_cnt + int(
            input("Write how many disposable cups of coffee do you want to add:"))
        # print_state()

    def perform_take(self):
        print("I gave you $", self.current_amount)

    def make_coffee(self, water, coffee, milk, amount):
        if self.validate_inventory(water, coffee, milk):
            print("I have enough resources, making you a coffee!")
            self.current_water = self.current_water - water
            self.current_coffee = self.current_coffee - coffee
            self.current_milk = self.current_milk - milk
            self.current_cup_cnt = self.current_cup_cnt - 1
            self.current_amount = self.current_amount + amount

    def validate_inventory(self, water, coffee, milk):
        status = True
        if self.current_water < water:
            print("Sorry, not enough water!")
            status = False
            # continue
        elif self.current_coffee < coffee:
            print("Sorry, not enough coffee!")
            status = False
            # continue
        elif self.current_cup_cnt < 1:
            print("Sorry, not enough cup!")
            status = False
            # continue
        elif self.current_milk < milk:
            print("Sorry, not enough milk!")
            status = False
        return status

    def perform_action(self):
        action_taken = input("Write action (buy, fill, take, remaining, exit):")
        while action_taken != "exit":
            if action_taken == "buy":
                coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                if coffee_type == "1":
                    self.make_coffee(250, 16, 0, 4)
                elif coffee_type == "2":
                    self.make_coffee(350, 20, 75, 7)
                elif coffee_type == "3":
                    self.make_coffee(200, 12, 100, 6)
                elif coffee_type == "back":
                    action_taken = input("Write action (buy, fill, take, remaining, exit):")
                    continue
                # print_state()
            elif action_taken == "fill":
                self.perform_fill()
            elif action_taken == "take":
                self.perform_take()
                self.current_amount = 0
                # print_state()
            elif action_taken == 'remaining':
                self.print_state()
            action_taken = input("Write action (buy, fill, take, remaining, exit):")


coffee_machine = Coffee()
