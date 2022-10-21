from .salmonella import Salmonella
"""
https://www.mev.wiki/attempts-to-trick-the-bots/kattana
https://etherscan.io/address/0x491e136ff7ff03e6ab097e54734697bb5802fc1c#code#F10#L9
"""
class TrapToken(Salmonella):
    def __init__(self) -> None:
        super().__init__("TrapToken")
        self.blocks_since_launch = 0

    def incrementBlock(self):
        self.blocks_since_launch += 1

    def transfer(self, amount: float, sender: int, receiver: int):
        if self.blocks_since_launch < 3 and 10 < amount:
            assert self.balances[sender] >= amount, f"{sender} has {self.balances[sender]} of {self.symbol}"

            self.balances[sender] -= amount
            out_amount = (amount * 0.1)
            self.balances[receiver] += out_amount
            
            return out_amount
        else:
            super().normal_erc20_transfer(amount, sender, receiver)
