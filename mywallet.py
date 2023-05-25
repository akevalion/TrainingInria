class Wallet:
    def __init__(self, initial: float = 0) -> None:
        self._balance = initial
        pass

    def balance(self) -> float:
        return self._balance

    def credit(self, amount: float) -> None:
        self.checkAmount(amount)
        self._balance += amount

    def checkAmount(self, amount: float) -> None:
        if amount < 0:
            raise NegativeAmountError () 

    def debit(self, amount: float) -> None:
        if amount > self._balance:
            raise NotEnoughMoney()
        self._balance -= amount

class NotEnoughMoney(Exception):
    pass

class NegativeAmountError(Exception):
    pass