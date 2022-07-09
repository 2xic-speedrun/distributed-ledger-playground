
from collections import defaultdict
from typing import DefaultDict
from numpy import reciprocal


class ERC20:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.balances = defaultdict(float)

    def transfer(self, amount: float, sender: int, receiver: int):
        return self._transfer(amount, sender, receiver)

    def _transfer(self, amount: float, sender: int, receiver: int):
        assert self.balances[sender] >= amount, f"{sender} has {self.balances[sender]} of {self.symbol}"

        self.balances[sender] -= amount
        self.balances[receiver] += amount

        return amount

    def mint(self, amount: float, receiver):
        self.balances[receiver] += amount

