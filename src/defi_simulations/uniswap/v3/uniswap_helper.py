from .utils import QValue
import numpy as np
import math

class UniswapHelper:
    def __init__(self, x, y, min_price, max_price):
        self.x = x
        self.y = y

        self.p_a = QValue(np.sqrt(max_price / self.x))
        self.p_b = QValue(np.sqrt(min_price / self.x))
        self.p_c = QValue(np.sqrt(self.price_x))

    def get_tick(self, price):
        return math.floor(
            math.log(price, 1.0001)
        )

    # sqrt(P) = sqrt this
    @property
    def price_x(self):
        return self.y / self.x

    @property
    def price_y(self):
        return self.x / self.y

    def get_liquidity(self, delta_x, delta_y):
        return min(self.L_x(delta_x), self.L_y(delta_y))

    def L_x(self, delta_x):
        max, min = self.min_max(self.p_c, self.p_b)
        max, min = max.value, min.value
        return (delta_x) * (max * min) / (max - min)

    def L_y(self, delta_y):
        max, min = self.min_max(self.p_c, self.p_a)
        max, min = max.value, min.value
        results = delta_y * (
            max - min
        )

        return results

    @property
    def max_price_current_min_max(self):
        return self.min_max(
            self.p_a,
            self.p_c
        )

    @property
    def min_price_current_min_max(self):
        return self.min_max(
            self.p_b,
            self.p_c
        )

    def min_max(self, a, b):
        if a.value > b.value:
            return a, b
        else:
            return b, a
