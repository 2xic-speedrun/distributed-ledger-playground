from ..utils.Wei import Wei
from ..utils.ERC20 import ERC20
from .cdp import cdp

"""
Based of what is written in https://makerdao.com/whitepaper/Dai-Whitepaper-Dec17-en.pdf
"""
class DAI(ERC20):
    def __init__(self) -> None:
        ERC20.__init__(self, "DAI")
        self.id = 0
        self.cdps: dict[int, cdp] = {

        }
    
    def create(self, amount: float):
        created_cdp = cdp('WEI', amount)
        created_cdp.id = self.id
        self.cdps[created_cdp.id] = created_cdp

        self.id += 1
        return created_cdp

    def fund(self, sender,  wei: Wei, id : int):
        wei.transfer(sender, self.cdps[id].address, self.cdps[id].collateral_ratio)
        self.mint(sender, self.cdps[id].amount)

    def pay_debt(self, sender, wei: Wei, id: int):
        pass

    

