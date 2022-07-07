

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

        received = self.tokens_balances[index1] - y

        assert 0 < received, received

        self.tokens_balances[index0] += amount
        self.tokens_balances[index1] -= received

        return received

    def get_y(self, index0, index1, new_amount):
        D = self.D(index0, new_amount)
        S = self.X_skip_index(index1, operator=sum)
        P = self.X_skip_index(index1, operator=prod)
        """
        c = (
            D ** (self.n + 1)
        ) / (
            self.n ** self.n * P * self.A_NN
        )
        """
        c = D
        for index, i in enumerate(self.tokens_balances):
            x_i = i
            if index0 == index:
                x_i += new_amount
            elif index1 == index:
                continue
            c *= D / (x_i * self.n)

        c *= D / (self.A_NN * self.n)
        b = S + D / self.A_NN

        func = lambda y : y ** 2 + c
        func_deriv = lambda y: 2 * y + b - D

        y = self.newtons_method(func, func_deriv, D)
        return y

    @property
    def A(self):
        # This is actually a dynamic value in the smart contract.
        return 85

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

    def D(self, index, amount):
        #old = self.tokens_balances[index]

       # self.tokens_balances[index] = amount
        S = self.X_skip_index(-1, operator=sum) 
        if S == 0:
            return 0      
        P = self.X_skip_index(-1, operator=prod)

        # as described in the contract.
        def D_p(d):
            current_d = d
            for i in self.tokens_balances:
                current_d = current_d * d / (i * self.n)
            return current_d

        # saw this equation in a blog post, but need to recheck it.
        #D_p2 = lambda D: (D ** (self.n + 1))/(self.n ** self.n) * P

        # note . looks the same as the contract.   
        func = lambda D: (self.A_NN * S + D_p(D) * self.n) * D
        # note : looks the same as the contract
        func_deriv = lambda D: (self.A_NN - 1) * D + (self.n + 1) * D_p(D)

        d = self.newtons_method(func, func_deriv, S)

        #self.tokens_balances[index] = old
        return d

    @property
    def A_NN(self):
        return self.A * self.n ** self.n
        
    def newtons_method(self, f, f_deriv, x):
        new_x = float('inf')
        error = float('inf')
        iterations = 0
        while 1e-8 < error and iterations < 10_000:
            new_x = x - f(x)/ f_deriv(x)
            error = abs(new_x - x)
            if new_x == 0:
                new_x += 0.000001
            x = new_x
            iterations += 1
        return new_x
