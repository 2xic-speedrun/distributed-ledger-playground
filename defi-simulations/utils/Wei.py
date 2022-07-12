from collections import defaultdict
from wsgiref.handlers import format_date_time


class Wei:
    def __init__(self) -> None:
        self.balances = defaultdict(float)
    
    def mint(self, user, amount):
        self.balances[user] += amount

    def transfer(self, from_addr, to_addr, amount):
        user_balance = self.balances[from_addr]
        assert user_balance > amount
        self.balances[from_addr] -= amount
        self.balances[to_addr] += amount

