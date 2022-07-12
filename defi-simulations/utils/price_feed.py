

from collections import defaultdict
from .singelton import singleton

@singleton
class PriceFeed:
    def __init__(self) -> None:
        self.price = defaultdict(float)

    def set_price(self, symbol: str, price:float):
        self.price[symbol] = price

    def get(self, symbol):
        return self.price[symbol]
        