## Whitepaper Curve

- Move efficient invariant than x*y=k
    - liquidity is concentrated based on the "internal oracle" price.
      - only move that price when the loss is smaller than part of the profits the system takes
      - This creates 5-10 higher liquidity than the Uniswap invariant.

## Transformed pegged invariants
  - Let `b =  (b_0, b_1, ...)` denote the balances in some smart contracts pools
  - Let `p = (p_0, p_1, ...)` denote teh price scale coefficient. 
  - Real balance is denoted *b* and transformed balances is *b'* can be converted between each other as.
  - `T` is an transformation function to move value to 1
   - `b` = T(b', p) = (b'_0p_0, b'_1 p_1, ...)
   - `b'`= T^(-1)(b, p) = (b_0/p_0, b1_p/1, ...) 
  - This can be represented as a hypersurface
    - Curve if the dimensions are 2 = hypersurface
    - This is plotted on page 2
  - I(b') = 0
    - invariant function is convenient to choose in a way such taht p0 = 1
      - The vector of all x should be such that I(x, x, ...) = 0
    - x_eq = (xeq, ceq, ...)
      - Equilibrium point
    - D = parametrized curve
      - D = Nx_eq
    - I(X_eq, D) = 0
## Quantification of a repegging loss
- Value of the portfolio without noise
  - X_cp = (
      product of (D/(Np_i)) 1/N
    )
  - When we change p, the price peg changes, but balances don't.

# CurveCrypto invariant
- Uses newton's method 
- Look at page 3-4 it has math, create a simulator for it.

# Algorithm for repegging
- 
