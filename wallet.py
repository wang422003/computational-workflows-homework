# wallet.py

class InsufficientAmount(Exception):
    def __init__(self, message="Insufficient Amount!"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message



class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if amount > self.balance:
            raise InsufficientAmount("Insufficient Amount!")
        self.balance = self.balance - amount

    def add_cash(self, amount):
        self.balance = self.balance + amount
