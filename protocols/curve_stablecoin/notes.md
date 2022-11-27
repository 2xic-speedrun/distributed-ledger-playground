https://github.com/curvefi/curve-stablecoin/blob/master/doc/curve-stablecoin.pdf

- Main idea is LLAMMA
  - Replacing liquidations with special purpose AMM

AMM For continuos liquidations
- Converts between collateral (ETH) to the stablecoin 
  - If price of collateral is high -> a user has deposits all in ETH, and as it goes lower, it convert to USD
  - Uses a external price oracle to be able to do this
Uses virtual balances like uniswap v3
- Amount in USD is x
- Amount in ETH is y
- Amplified constant product invariant
  - I = (x + f)(y + g)
  - x' = x x + f
  - y' = y + g
  - i.e I = x'y'
- f and g does not stay constant, and will change with the external price oracle.
- So will also the invariatn I
  - (top price of the band)      = (A - 1)
    / (bottom price of ban)         / A
- Requirements for the A
    f = (p_0) ** 2 * A * y_0
        / (top price of the band)
    g = (top price of the band) * (A - 1 ) * y_0
        / p_0
- y_0 is a p_0 dependent measure of deposits in the current band (denominated in ETH)
- I = p_0* A**2 * y_0 ** 2
- Typically we know top price, and price, and bottom price, constant A and deposits in x and y
- We need y_0 and can find it with equation 7 in the paper (quadratic one)

-----
LLAMMA vs Stablecoin
- Stablecoin is a CDP
- If ETH goes down relatively slowly then the ETH is converted into enoughs stablecoin to cover the closing of the CDP
  - Which can be done by the user or an external users
----
Automatic stabilizer and monetary policy
- If P_s > 1 because there is a high demand of the stablecoin
  - Peg-keeping reserve will formed by asymmetrical deposits into stableswap
- If P_s < 1 the PegKeeper is allowed to burn the stablecoin


----

Good threads
- https://twitter.com/0xfoobar/status/1595085743461961730?s=12&t=ArB0iR6cuBGY8SJjjJbTHA&utm_source=pocket_saves
- https://twitter.com/0x94305/status/1595292889298321408?s=12&t=qAtm2xLye3WiO4yroKZ6iQ&utm_source=pocket_saves
  - 