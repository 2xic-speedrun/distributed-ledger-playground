from ...uniswap.v1.uniswap_erc20 import UNISWAP_ADDRESS
from ...utils.ERC20 import ERC20

class Salmonella(ERC20):
    def __init__(self, name="Salmonella") -> None:
        ERC20.__init__(self, name)

    def transfer(self, amount: float, sender: int, receiver: int):
        assert self.balances[sender] >= amount, f"{sender} has {self.balances[sender]} of {self.symbol}"

        if sender == UNISWAP_ADDRESS:
            return self.normal_erc20_transfer(amount, sender, receiver)
        else:
            self.balances[sender] -= amount
            out_amount = (amount * 0.1)
            self.balances[receiver] += out_amount
            
            return out_amount

    def normal_erc20_transfer(self, amount ,sender, receiver):
         return super().transfer(amount, sender, receiver)
