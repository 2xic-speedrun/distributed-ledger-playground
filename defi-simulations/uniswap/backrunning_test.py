import unittest
from .simulator import UniswapPair

class BackrunningAttack(unittest.TestCase):
    """
        This is more or less the same as a sandwitch with one big 
        caveat, it is only preformed when a new pair is created. 
    """
    def setUp(self) -> None:
        self.uniswap = UniswapPair(
            10,
            10
        )
        # the backrun value
        self.backrun_amount = 5
        self.original_value = self.uniswap.swap_reserve0(
            self.backrun_amount
        )


    def test_trader_after_backrun(self):
        # new buyer
        self.uniswap.swap_reserve0(2)

        sell = self.uniswap.swap_reserve1(self.original_value)
        assert 0 < (sell - self.backrun_amount)


