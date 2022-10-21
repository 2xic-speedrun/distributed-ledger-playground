# Seigniorage Shares

Problem they try to solve: making coin value stable.


## (Proposed) Solution
Elastic money supply based on market value, has the following challenges
- How to have the price information delivered in a trustless way ?
- How often should one rebase the money supply ? 

Formula is in `elastic_coin_supply.py`



### How not to rebase the money supply
- You should not just rebase the wallet balance by q_i/q_{i - 1}

### Better way (Seigniorage Shares)
Two types on money: coin and shares.

\delta_i is distributed to people holding shares.
- When supply of coin increases then the amount it is exchanged for shares
  - More coins, less shares
  - Users have to bid on coins with shares (coin auction) quantity of shares for coin and the minimum rate.
    - That means delta_i / shares bid are destroyed.

- When supply of coin needs to decrease, coin are exchanged for shares.
  - Less coins, more shares
    - Users have to bid on shares with coins (share auction) and the minimum coin / share price rate.

### How to know the price
- Schelling point
- 