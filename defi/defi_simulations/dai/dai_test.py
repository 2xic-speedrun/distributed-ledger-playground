import unittest
from .dai import DAI
from ..utils.Wei import Wei
from ..utils.price_feed import PriceFeed

class TestDai(unittest.TestCase):
    def test_creation_example_1(self):
        test_user = 0x42
        wei = Wei()
        wei.mint(
            test_user,
            500
        )
        dai = DAI()
        cdp = dai.create(
            100
        )
        dai.fund(
            test_user,
            wei,
            cdp.id
        )
        assert cdp.payback(365) == 101

    def test_collateral_to_debt(self):
        test_user = 0x42
        price_feed = PriceFeed()
        wei = Wei()
        wei.mint(
            test_user,
            500
        )
        dai = DAI()
        cdp = dai.create(
            100
        )
        eth_price = 0.375
        price_feed.set_price(
            "wei",
            eth_price
        )
        assert cdp.collateral_to_debt == 1.5
        assert cdp.can_be_liquidated == False
        
        eth_price_after_price_drop = eth_price * 0.9
        price_feed.set_price(
            "wei",
            eth_price_after_price_drop
        )
        assert cdp.collateral_to_debt == 1.35
        assert cdp.can_be_liquidated == True

        
