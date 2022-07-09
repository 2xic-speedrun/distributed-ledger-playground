import matplotlib.pyplot as plt
import numpy as np

"""
The price curve of a Uniswap pool
"""

x = np.linspace(0, 10)
constant = 10 - x
uniswap = 10 / x

plt.plot(x, constant)
plt.plot(x, uniswap)

plt.show()
