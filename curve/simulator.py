

from itertools import product
from operator import mul
from numpy import prod

from pytest import skip

class CurveSimulator:
    def __init__(self, tokens_balance: list[float]) -> None:
        self.tokens_balances = tokens_balance 
        self.rates = (1, 1)
        self.n = len(self.tokens_balances)
        self.amplification = 50

    def swap(self, index0, index1, amount):
        assert index0 != index1, "cannot swap between same index"
        y = self.get_y(index0, index1, amount)

        assert 0 < y, y

        dy = self.tokens_balances[index1] - y

        assert 0 < dy, dy

        self.tokens_balances[index1] -= dy
        self.tokens_balances[index0] += amount

    def get_y(self, index0, index1, amount):
        D = self.D
        S = self.X_skip_index(index1, operator=sum)
        P = self.X_skip_index(index1, operator=prod)
        c = (
            D ** (self.n + 1)
        ) / (
            self.n ** self.n * P * self.ANN
        )
        b = S + D / self.ANN
        print((b, D, c, self.A))

        func = lambda y : y ** 2 + c
        func_deriv = lambda y: 2 * y + b - D

        y = self.newtons_method(func, func_deriv, D)
        return y

    @property
    def A(self):
        # This is actually a dynamic value in the smart contract.
        return 10

    @property
    def X_p(self):
        return [
            b * self.rates[index] for index, b in enumerate(self.tokens_balances)
        ]

    @property
    def X(self):
        return self.X_skip_index(-1, operator=prod)        
        
    def X_skip_index(self, skip_index, operator):
        return operator([
            i for index, i in enumerate(self.tokens_balances) if index != skip_index
        ])

    @property
    def D(self):
        S = self.X_skip_index(-1, operator=sum)    
        D_p = lambda D: (D ** (self.n + 1))/(self.n ** self.n) * S
        func = lambda D: (self.ANN * S + self.n * D_p(D)) * D
        func_deriv = lambda D: (self.ANN - 1) * D + (self.n + 1) * D_p(D)

        d = self.newtons_method(func, func_deriv, S)
        return d

    @property
    def ANN(self):
        return self.A * self.n ** self.n
        
    def newtons_method(self, f, f_deriv, x):
        new_x = float('inf')
        error = float('inf')
        iterations = 0
        while 1e-8 < error and iterations < 10_000:
            new_x = x - f(x)/ f_deriv(x)
            error = abs(new_x - x)
            x = new_x
            iterations += 1
        return new_x






