import unittest
from unittest import result
from curve.simulator import CurveSimulator

from uniswap.simulator import UniswapPair
import numpy as np


class TestCurveSimulator(unittest.TestCase):
    def test_newton(self):
        curve = CurveSimulator(
            [50, 50]
        )
        results = curve.newtons_method(
            lambda x: x,
            lambda _x: 10,
            1
        )
        assert np.allclose(results, 0, atol=1e-5)

    def test_swap(self):
        curve = CurveSimulator(
            [50, 50]
        )
        curve.swap(index0=0, index1=1, amount=1)

        print(curve.tokens_balances)
        assert 1 ==2

if __name__ == '__main__':
    unittest.main()
