# [RAI](https://raw.githubusercontent.com/reflexer-labs/whitepapers/master/English/rai-english.pdf)

Notes from me reading the whitepaper. Note that the notes are only related to how RAI works, and not a summary of the entire paper. Notes are written in the order they appear in the paper.

## Abstract
- Protocol that automatically reacts to market forces in order to modify the target value of an collateralized asset
- "Reflex index"
  - "dampened version of the underlying collateral".
- The paper will outline how "Relfex indexes" can be used a low volatility collateral.

## Overview of Reflex Indexes
- Reflex index is not meant to maintain a specific peg. It's meant to dampen the volatility of it's collateral.

### The redemption price
- The value of one debt unit (or coin ) in the system.
- Should be an internal accounting tool, and is different form the market price.
  - Stablecoins like USDC have the redemption price as 1 USD = 1 USDC. 
  - However, the market price for USDC can sometimes be both greater or lower than the redemption price.
    - This creates arbitrage opportunities. 
      - Is the market price higher than the redemption price ? 
        - Convert USD to USDC, and sell with profits on the open market.
      - Is the market price lower than the redemption price ?
        - Buy USDC and redeem it for USD. 
- Reflex indexes also have a redemption price that the system targets, but this will *not* be fixed. It's designed to be influenced by market forces.
  - This again creates arbitrage opportunities. 

## Design Philosophy and Go-to-market strategy
- Security , Stability and Speed of delivery.
- They build upon Multi-Collateral DAI design with an autonomous rate setter, and an Oracle Network Medianizer (what ?) which is fancy word for saying they get price feeds from multiple channels.

## Monetary Policy Mechanisms

### (Introduction to ) Control theory
- You put the Car in cruise control. Given control over a system input (gas pedal) and to system output (gas speed), we can measure the error and apply it for the car to keep the setpoint as the road / terrain etc changes.
  - PID controller
    - Controller output = Proportional Term + Integral Term + Derivative term
  - P(roportional term) is directly proportional to the deviation
    - Is the deviation huge in the Cruise example the gas / break pedal to the floor
  - I(ntegral term) sees how long has a deviation persisted by taking the integral of the deviation over time. 
    - Aims to eliminate persistent deviation from the setpoint. The cruise control setpoint has been 1 mph higher than the cars speed for a few minutes.
  - D(erivative term) is the part of the controller which looks at how fast the deviation is changing (is it growing, or shrinking ?). Takes the derivative of the deviation.
    - Responses when the deviation is growing. Speed up if the cruise control setpoint is higher than the cars speed, and slow down if the speed is higher than the setpoint.
- Redemption price chan be changed by PID controllers.
    - Existing bank monetary policies like the Taylor Rule are said to be approximations of PID controllers (ref 5. in the paper). 

## Redemption rate feedback mechanism
- The system component in charge of changing the reflex index redemption price.
- Redemption rate is the rate of change of the redemption price. This is the rate the authors want the users to respond to. 
  - Set by a feedback mechanism that governance can fine-tune, or allow to be fully automated.
- The goal of the feedback mechanism is to maintain equilibrium between the redemption price and the market price by using the redemption rate to counter shifts in the market forces.
- Example 1 - Index's market price is higher than it's redemption price
    - Response: An negative rate will be set to decrease the redemption price, and making the systems debt cheaper.
    - Rational: The decrease in redemption will likely discourage people from holding the indexes, and encourage "SAFE" holders to generate more debt that is then sold on the market. Supply and demand should be balanced.
    - Over time this response time should (ideally) be short, but at launch it might take time.
-  Example 2 - index's price is lower than the redemption price. 
   -  Response: Positive redemption rate. Debt will become more expensive.
   - Rational: Debt will become more expensive, and the SAFEs will go down, SAFE creators will pay back debt. Users start to hoard indexes with the expectation that they will increase in value.

## Feedback mechanism algorithm
- When the index is launched it's set to an arbitrary redemption price 'rand'
- when the market price rises from 'rand' to 'rand' + x
  - The feedback mechanism reads the new market price, it calculates the P term that is (-1 * ((rand + x) / rand))
    - Negative in order to decrease the redemption price and in turn reprice the indexes so that they become cheaper.
  - Then it calculates the I term by adding the past deviations from the last deviationInterval seconds
  - The mechanism sums the P and I and calculates the per-second redemption rate r that slowly start to decrease the redemption price.
    - SAFE creators will flood the market with more indexes when they realize they can generate more debt.
  - After n seconds the mechanism detect that the deviation between market and redemption price is negligible (based on a noise parameter).
    - Then the system sets r to zero, and keeps the redemption price where it is.

## Feedback mechanism tuning
- Hard to tune a PID controller in production on a decentralized financial system. Also risky.
  - Authors suggest running on computer modeling and simulation.

## Money market setter
- Borrowing rate (interest rate applied when generating indexes) fixed or capped. 
  - Rai only modifies the redemption price.


## Global settlement
- Looks like a failsafe method. 

## Governance
- They have written multiple sections on the Governance, but skipping it for now.

## Oracles
- Need to know price of 3 assets
  - index
  - protocol token
  - whitelisted collateral type
- Oracle network medianizer
  - Smart contract that reads prices from multiple sources which are not directly controlled by the governance (Uniswap). 

## Safes
- Anyone can deposit and leverage their crypto collateral inside Safes. While a SAFE is opened it will continue accruing debt according to the deposited collateral's borrowing rate.
- As the SAFE creator pays back their debt, they will be able to withdraw more and more of their locked collateral.

### Lifecycle
- Deposit collateral in the SAFE
- Generates indexes backed by the SAFE's collateral
  - User specifies how many indexes they want to generate.
  - The system creates an equal amount of debt that start to accrue according to the collateral's borrowing rate
- Pay back the SAFE debt.
- Withdraw collateral

### Liquidations
- To keep the system solvent and cover the outstanding debt.
  - The system can liquidate if the collateralization falls under a certain threshold.
  - Anyone can trigger a liquidation.
    - The collateral it sold off in a collateral auction
### Liquidation insurance
- Smart contract that automatically adds more collateral to prevent liquidations.

## Collateral auctions
- System coins used to settle bad debt.
  - buyCollateral in order to exchange system coins for collateral
    - sold at discount compared to it's latests recorded market price

## Debt auctions
- mint more protocol tokens, and sell them for indexes that can nullify the systems remaining bad debt.
- Automated
- The auction is restarted if no bids places, and every time it's restart the system will offer more protocol tokens for the same amount of indexes.

## Insurance fund

## Surplus auctions






































