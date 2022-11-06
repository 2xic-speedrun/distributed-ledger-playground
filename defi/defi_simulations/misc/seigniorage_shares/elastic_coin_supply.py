from curses import newpad
from ...utils.price_feed import PriceFeed
from ...utils.static_price_feed import StaticPriceFeed


class ElasticCoinSupply:
    def __init__(self, q_0: float, price_feed: StaticPriceFeed) -> None:
        self.q = self.q_0
        self.p = self.price_feed.get_price()
        self.price_feed: StaticPriceFeed = price_feed

    def rebase(self):
        new_price = self.price_feed.get_price()
        delta_p = new_price / self.p
        new_supply = self.q * delta_p

        rebase_amount = (new_supply - self.q)

        self.p = new_price
        self.q = new_supply

        return rebase_amount
        