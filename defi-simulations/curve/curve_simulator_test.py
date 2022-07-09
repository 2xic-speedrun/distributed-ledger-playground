import unittest
from .simulator import CurveSimulator
import numpy as np


class TestCurveSimulator(unittest.TestCase):
    def test_newton(self):
        curve = CurveSimulator(
            [50, 50]
        )
        results = curve.newtons_method(
            lambda x: x,
            lambda _x: 1,
            1
        )
        assert np.allclose(results, 0, atol=1e-5)

    def test_newton_2(self):
        curve = CurveSimulator(
            [50, 50]
        )
        results = curve.newtons_method(
            lambda x: 1 - x ** 2,
            lambda x: - 2 * x,
            1
        )
        assert np.allclose(results, 1, atol=1e-5)

    def test_swap(self):
        curve = CurveSimulator(
            [50, 50]
        )
        curve.swap(index0=0, index1=1, amount=1)
        
        assert np.allclose(51, curve.tokens_balances[0])
        assert np.allclose(49.5073, curve.tokens_balances[1])

if __name__ == '__main__':
    unittest.main()
