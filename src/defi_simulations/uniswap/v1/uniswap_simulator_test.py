import unittest

from .uniswap_simulator import UniswapPair
import numpy as np


class TestSimulator(unittest.TestCase):
    def test_swap_reserve_0(self):
        amm = UniswapPair(
            10,
            10
        )
        amm.swap_reserve0(5)
        assert amm.reserve0 == 15
        assert np.allclose(amm.reserve1, 6.6666666)
        assert amm.price_0 < amm.price_1

    def test_swap_reserve_1(self):
        amm = UniswapPair(
            10,
            10
        )
        amm.swap_reserve1(5)
        assert amm.reserve1 == 15
        assert np.allclose(amm.reserve0, 6.6666666)
        assert amm.price_1 < amm.price_0 

        amm.swap_reserve1(5)
        assert amm.reserve1 == 20
        assert np.allclose(amm.reserve0, 5)
        assert amm.price_1 < amm.price_0 

    def test_price(self):
        amm = UniswapPair(
            10,
            10
        )
        assert amm.price_0 == 1
        assert amm.price_1 == 1

if __name__ == '__main__':
    unittest.main()
