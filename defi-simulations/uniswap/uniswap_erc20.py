from .simulator import UniswapPair
from utils.ERC20 import ERC20

UNISWAP_ADDRESS = 0x42222222222222222

class UniswapErc20(UniswapPair):
    def __init__(self, token1: ERC20, token2: ERC20) -> None:
        self.token1 = token1
        self.token2 = token2
        self.address = UNISWAP_ADDRESS
        UniswapPair.__init__(
            self,
            self.token1.balances[self.address],
            self.token2.balances[self.address]
        )

    def swap_reserve0(self, caller, amountIn: float):
        amount_sent = self.token1.transfer(
            amountIn,
            caller,
            self.address
        )
        amount_out = super().swap_reserve0(amount_sent)
        self.token2.transfer(
            amount_out,
            self.address,
            caller,
        )
        return amount_out


    def swap_reserve1(self, caller, amountIn: float):
        amount_sent = self.token2.transfer(
            amountIn,
            caller,
            self.address
        )
        amount_out = super().swap_reserve1(amount_sent)
        self.token1.transfer(
            amount_out,
            self.address,
            caller,
        )
        return amount_out
