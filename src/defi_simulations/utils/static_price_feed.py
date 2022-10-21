

from src.defi_simulations.utils.price_feed import PriceFeed


class StaticPriceFeed:
    def __init__(self, symbol) -> None:
        self.price_feed = PriceFeed()
        self.symbol = symbol

    def get_price(self):
        return self.price_feed.get(self.symbol)

    def set_price(self, price):
        self.price_feed.set_price(self.symbol, price)
    

    