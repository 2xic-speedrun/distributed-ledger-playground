import unittest
from ...uniswap.v1.uniswap_erc20 import UNISWAP_ADDRESS, UniswapErc20
from ...utils.ERC20 import ERC20
from .salmonella import Salmonella

class TestSalmonella(unittest.TestCase):
    def setUp(self) -> None:
        self.mev_bot = 0x44
        self.user = 0x22
    
        self.uniswap_pool = UNISWAP_ADDRESS
    
        self.eth = ERC20("ETH")
        self.salmonella = Salmonella()

        self.eth.mint(1000, self.uniswap_pool)
        self.salmonella.mint(1000, self.uniswap_pool)

        self.eth.mint(
            10,
            self.mev_bot,
        )

        self.eth.mint(
            10,
            self.user,
        )

        self.uniswap_pool = UniswapErc20(
            self.eth,
            self.salmonella,
        )

    def test_salmonella_makes_mev_bot_sad(self):
        amount = 3

        swapped_output = self._front_run_asset1(amount)

        self.uniswap_pool.swap_reserve0(self.user, amount)

        sell = self.uniswap_pool.swap_reserve1(self.mev_bot, swapped_output)

        # mev bot lost money, pool has more money.
        assert (sell - amount) < 0
 
    def _front_run_asset1(self, amount):
        return self.uniswap_pool.swap_reserve0(self.mev_bot, amount)
