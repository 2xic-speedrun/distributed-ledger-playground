import numpy as np


class ConcentratedLiquidity:
    def __init__(self, invariant):
        self.invariant = invariant

        self.x_real = 0
        self.y_real = 0

        self.position_a = 100
        self.position_b = 100

    def virtual_reserve_y(self, x):
        P = (self.L / x) ** 2
        x = self.L ** 2 / (x + self.L / np.sqrt(self.position_b))

        y = self.L * (np.sqrt(P ) - np.sqrt(self.position_a))
        return y

    def real_reserve_y(self, x):
        return self.invariant / x

    @property
    def L(self):
        return np.sqrt(self.invariant)
