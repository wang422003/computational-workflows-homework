# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        raise NotImplementedError

    def spend_cash(self, amount):
        raise NotImplementedError

    def add_cash(self, amount):
        raise NotImplementedError
