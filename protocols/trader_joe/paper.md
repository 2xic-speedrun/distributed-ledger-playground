[paper](https://raw.githubusercontent.com/traderjoe-xyz/LB-Whitepaper/main/Joe%20v2%20Liquidity%20Book%20Whitepaper.pdf)

- Joe v1 started as a Uniswap v2 clone with liquidity contracts
- Joe v2 -> Liquidity book
  - Prices are grouped into discrete price bins
  - Reserves can be exchanged for the constant exchange rate for a given bin
    - P = delta_y / delta_x
    - Price = rate of change in y per x change reserve
    - Bin liquidity(L) is defined as P * x + y = L   
  -Bin composition
    - Composition is defined as C = y / L
    - y = C * L
    - x = L / P * (1 - C)
    - https://research.thetie.io/trader-joes-new-amm-liquidity-book/
    - https://coinmarketcap.com/community/articles/39056
      - One bin establish the market price
        - It's the lowest price bin that contains reserves of both assets
        - LPs can allocate to specific bins
        - Each bin has it's own bounding curve
        - 

