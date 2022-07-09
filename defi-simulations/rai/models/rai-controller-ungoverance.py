# Based of notes from https://community.reflexer.finance/t/rai-controller-ungovernance/208
import numpy as np
import matplotlib.pyplot as plt

def plot(x, market_price, market_fluctuation, Kp, rai_price_target):
    # Kp = P-controller 
    # It's not specified, but let's assume the RAI/USD TWAP is a sin curve
    # The deviation is specified to be 1%
    price_function = (market_fluctuation * market_price) * np.sin(x * 1/2) + market_price
    error = (rai_price_target - price_function)
    redemption_rate = (Kp * error)

    # not sure if this is how it is supposed to be.
    # the redemption price is as far as I understand set by the protocol (i.e static)
    # but the ploted value in the forum is not static.
    # ref. https://docs.reflexer.finance/faq
    redemption_price = rai_price_target + Kp * (price_function - rai_price_target)

    return price_function, redemption_price, redemption_rate, error

"""
Plots to re-generate
1. Redemption and market price
2. Absolute error
3. Redemption rate
"""

X = np.linspace(0, 20, num=15)

fig, axs = plt.subplots(3, 2)

for index, rate in enumerate([3, 6]):
    price, redemption_price, redemption, error = plot(
        X,
        rate,
        0.01,
        7.5e-8,
        rai_price_target=rate
    )
    axs[0, index].plot(X, price)
    axs[0, index].plot(X, redemption_price, color="orange")
    axs[1, index].plot(X, error)
    axs[2, index].plot(X, redemption)
plt.show()


