from utils.price_feed import PriceFeed

class cdp:
    def __init__(self, collateral_type, amount) -> None:
        self.id = None
        self.collateral_type = collateral_type
        self.amount = amount
        self.eth_deposited = self.amount * 4
 
        self.stability_fee = 0.01
        self.liquidation_ratio = 1.45
        self.penalty_ratio = 1.05

    @property
    def address(self):
        return self.id

    @property
    def collateral_ratio(self):
        return self.eth_deposited
    
    def payback(self, days):
        return (1 + (0.01/365)*days) * self.amount

    @property
    def collateral_to_debt(self):
        price = PriceFeed().get("wei")
        return (self.eth_deposited * price) / (self.amount)

    @property
    def can_be_liquidated(self):
        return self.collateral_to_debt < self.liquidation_ratio
