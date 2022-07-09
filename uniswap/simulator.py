import numpy as np

class UniswapPair:
    def __init__(self, reserve0: float, reserve1: float, blockTime: float=0):
        self.reserve0 = reserve0
        self.reserve1 = reserve1
        self.k = reserve0 * reserve1
        self.accumulator = 0
        self.blockTime = blockTime        

    @property
    def price_0(self):
        return self.reserve1 / self.reserve0

    @property
    def price_1(self):
        return self.reserve0 / self.reserve1
    
    def swap_reserve0(self, amountIn: float):
        assert amountIn <= self.reserve0
        alpha = amountIn / self.reserve0

        new_reserve0 = self.reserve0 + amountIn 
        out = self.reserve1 * (alpha / (1 + alpha))
        new_reserve1 = self.reserve1 - out

        self._update(new_reserve0, new_reserve1)

        return out
    
    def swap_reserve1(self, amountIn: float):
        assert amountIn <= self.reserve0
        beta = amountIn / self.reserve1

        out = self.reserve0 * (beta / (1 + beta))
        new_reserve0 = self.reserve0 - out
        new_reserve1 = self.reserve1 + amountIn

        self._update(new_reserve0, new_reserve1)

        return out

    def _update(self, new_reserve0, new_reserve1):
        assert 0 < new_reserve0
        assert 0 < new_reserve0
        self.reserve0 = new_reserve0
        self.reserve1 = new_reserve1
        invariant = self.reserve0 * self.reserve1

        assert np.allclose(invariant, self.k), "invariant is broken {invariant}".format(invariant=invariant)

