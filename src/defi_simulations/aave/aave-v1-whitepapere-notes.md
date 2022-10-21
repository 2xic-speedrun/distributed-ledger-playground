https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf

- Interest rate is dynamic for borrowers and lenders
- Lending pools
  - Contains reserves from multiple currencies.
  - Total amount defined in ETH is the total liquidity
  - Reserve accepts deposits by lenders
  - Borrowers can borrow if they put a greater amount as collateral
    - The amount possible to borrow is depends on the values in the reserves.
    - Every reserve has a loan to value ratio.
- Positions
  - Can be opened with a variable or stable rate
  - No repayment schedule
    - Partial or full repayment can be done at anytime.
- Liquidations
  - If the value of the collateral drops below a given (liquidation) threshold
  - Liquidation bonuses are given out to incentives liquidators to buy the collateral at a discounted price
- All positions has a defined health factor defined by equation H_f on bottom of page 2
  - if H_f < 1 then the loan can be liquidated.

- Interest rate is defined on page 6 section 2.5
- Many (nice) flow charts describes the flow of the system.
- Tokenization of the protocol is described on page 16 , section 3.8
- 