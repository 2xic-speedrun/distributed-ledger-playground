import matplotlib.pyplot as plt
import numpy as np

"""
The price curve of a Uniswap pool
"""

x = np.linspace(0, 10)
k = 100
y = k / x

plt.plot(x, y)
plt.show()
