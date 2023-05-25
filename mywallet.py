class Wallet:
    def __init__(self, initial: float = 0) -> None:
        self._balance = initial
        pass

    def balance(self) -> float:
        return self._balance

    def credit(self, amount: float) -> None:
        self._balance += amount

    def debit(self, amount: float) -> None:
        if amount > self._balance:
            raise NotEnoughMoney()
        self._balance -= amount

class NotEnoughMoney(Exception):
    pass