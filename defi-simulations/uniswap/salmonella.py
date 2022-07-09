from uniswap.uniswap_erc20 import UNISWAP_ADDRESS
from utils.ERC20 import ERC20

class Salmonella(ERC20):
    def __init__(self) -> None:
        ERC20.__init__(self, "Salmonella")

    def transfer(self, amount: float, sender: int, receiver: int):
        assert self.balances[sender] >= amount, f"{sender} has {self.balances[sender]} of {self.symbol}"

        if sender == UNISWAP_ADDRESS:
            return super().transfer(amount, sender, receiver)
        else:
            self.balances[sender] -= amount
            out_amount = (amount * 0.1)
            self.balances[receiver] += out_amount
            
            return out_amount
