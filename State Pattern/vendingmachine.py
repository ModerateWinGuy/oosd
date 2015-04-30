"""
Vending machine states
- Waiting for right amount of money
- right amount of money entered, waiting for choice
- vending choice
- Choice dispenced, back to waiting
"""


class VendingMachine():

    def __init__(self):
        self.state = Waiting()
        self.current_balance = 0.0

    def enter_money(self, amount_entered):
        self.current_balance += amount_entered

    def select_choice(self):
        choice = input()

    def switch(self):
        self.state = self.state.switch()


class Waiting():

    def __init__(self, vending_machine):
        self.machine = vending_machine

    def switch(self):
        if self.machine.current_balance < 0:
            return MoneyEntered()
        else:
            return Waiting()


class MoneyEntered():

    def __init__(self, vending_machine):
        self.machine = vending_machine
        self.item_price = 2

    def switch(self):
        if self.machine.current_balance >= self.item_price:
