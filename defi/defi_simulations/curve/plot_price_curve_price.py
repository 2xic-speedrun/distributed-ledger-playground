import matplotlib.pyplot as plt
import numpy as np

constants = 250

x = np.linspace(0, constants)
constant = constants - x
constant[constant < 0] = 0

uniswap = constants / x


plt.plot(x, constant, label="Constant")
plt.plot(x, uniswap, label="Uniswap")

from curve_invariant import x, y, F
plt.contour(x, y, F, [0])


plt.legend(loc="upper left")
plt.show()
