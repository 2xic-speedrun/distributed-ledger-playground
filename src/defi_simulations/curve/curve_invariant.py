import numpy as np
# To making it plotable we can only have 2 pools

X = np.linspace(0, 200, num=1000)
Y = np.linspace(0, 200, num=1000)

x, y = np.meshgrid(X, Y)


# Constants for this swap
N = 2
D = 50
A = 50

gamma = 1e-3
N_sq = N ** N
Ann = A * N_sq

PROD_POOL = x * y
SUM_POOL = x + y

K_0 = (PROD_POOL * N_sq) / (D ** N)
K = A * K_0 * ( gamma * 2) / ( gamma + 1 - K_0) ** 2

F = K * D ** ( N - 1) * SUM_POOL + PROD_POOL - K * D**N - (D/ N) **N


#print(F)



