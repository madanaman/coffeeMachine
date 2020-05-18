class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, start_dollars, start_cents):
        self.dollars = start_dollars
        self.cents = start_cents

    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents + deposit_cents > 99:
            self.dollars = self.dollars + (self.cents + deposit_cents) // 100
            self.cents = (self.cents + deposit_cents) % 100
        else:
            self.cents = self.cents + deposit_cents

        self.dollars = self.dollars + deposit_dollars


# a = PiggyBank(0, 99)
# a.add_money(0, 50)
# print(a.dollars, a.cents)
