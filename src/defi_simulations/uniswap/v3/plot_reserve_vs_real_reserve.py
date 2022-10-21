import matplotlib.pyplot as plt
import numpy as np
from .concentrated_liquidity import ConcentratedLiquidity

concentrated = ConcentratedLiquidity(100)

X = np.linspace(0, 10, num=100)
y = np.linspace(0, 10, num=100)

virtual_reserve = concentrated.virtual_reserve_y(
    X,
)
real_reserve = concentrated.real_reserve_y(
    X
)

print(virtual_reserve)

plt.plot(virtual_reserve, label="Virtual")
plt.plot(real_reserve, label="Real")

plt.xlim(-1, 10)

plt.legend(loc="upper left")
plt.show()
