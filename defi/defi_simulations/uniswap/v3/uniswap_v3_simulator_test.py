import unittest
from .uniswap_v3_simulator import UniswapV3Simulator

from .utils import value_to_q96, q96
from .uniswap_helper import UniswapHelper
import numpy as np


class TestUniswapV3Simulator(unittest.TestCase):
    def test_liquidity(self):
        amm_helper = UniswapHelper(
            x=1,
            y=5000,
            min_price=4545,
            max_price=5500
        )

        amm = UniswapV3Simulator(
            amm_helper
        )
        amm.deposit()
        print(amm.x)
        print(amm.y)

        delta_price = amm.price_diff(42)
        print(delta_price)

        swap_x, swap_y = amm.swap_0(amm_helper.p_c.value + delta_price)
        print(swap_x, swap_y)

        unittest.expectedFailure()
