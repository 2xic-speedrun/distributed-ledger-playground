import numpy as np
import math

from src.defi_simulations.uniswap.v3.uniswap_helper import UniswapHelper
from .utils import q96, QValue


class UniswapV3Simulator:
    def __init__(self, amm_helper: UniswapHelper):
        self.amm_helper = amm_helper

    def deposit(self):
        # how much x, and y tokens needs to be deposited ?
        # L is calculated from the uniswap helper

        # eq. 6.5 in paper
        # eq. 6.6 in paper

        # it is also described here
        # https://uniswapv3book.com/docs/milestone_1/calculating-liquidity/#token-amounts-calculation-again

        max_price, min_price = self.amm_helper.max_price_current_min_max
        max_price, min_price = max_price.value, min_price.value
        self.x = self.L * (max_price - min_price) / (max_price * min_price)

        max_price, min_price = self.amm_helper.min_price_current_min_max
        max_price, min_price = max_price.value, min_price.value
        self.y = self.L * (max_price - min_price)

    def price_diff(self, delta_y):
        # L is provided into the smart contract.
        return delta_y / self.L

    def swap_0(self, next_price):
        """
        x = (L * (np.sqrt(p_b) - np.sqrt(p_a))) / 
                (np.sqrt(p_b) * np.sqr(p_a))

        p_a = next_price
        p_b = current_price

        y = L * (sqrt(p_b) - sqrt(p_a))        

        p_a = next_price
        p_b = current_price
        """
        max_p, min_p = self.amm_helper.min_max(
            self.amm_helper.p_c,
            QValue(next_price)
        )
        max_p, min_p = max_p.value, min_p.value
        max_p = np.sqrt(max_p)
        min_p = np.sqrt(min_p)
        
        x = self.L * (
            max_p - min_p
        ) / (
            max_p * min_p
        )
        y = self.L * (max_p - min_p)

        return (
            x,
            y
        )

    @property
    def L(self):
        return self.amm_helper.get_liquidity(
            self.amm_helper.x,
            self.amm_helper.y
        )
