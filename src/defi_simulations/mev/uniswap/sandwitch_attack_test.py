import unittest

from .sandwich_attack import SandwichAttack


class TestSandwich(unittest.TestCase):
    def test_front_run(self):
        sandwich = SandwichAttack()
        profits = sandwich.trade_asset_1(
            2
        )
        assert 0 < profits
