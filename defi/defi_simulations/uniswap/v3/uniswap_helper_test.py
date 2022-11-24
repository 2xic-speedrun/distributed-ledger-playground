import unittest
from .uniswap_helper import UniswapHelper
import numpy as np


class TestUniswapHelper(unittest.TestCase):
    def test_liquidity(self):
        amm = UniswapHelper(
            x=1,
            y=5000,
            min_price=4545,
            max_price=5500
        )
        assert amm.price_y == 1/5000
        assert amm.price_x == 5000
        assert amm.get_tick(amm.price_x) == 85176

        """
        Test cases provided https://uniswapv3book.com/docs/milestone_1/calculating-liquidity/
        does not seem to work as described
        """
        assert (
            amm.L_y(5000)
        ) == 1517882343751509868544

        assert (
            amm.L_x(1)
        ) == 1519437308014769733632
