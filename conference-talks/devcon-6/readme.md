Some talks I liked by looking at slides :)

# why-account-abstraction-is-a-game-changer-for-dapps
- Problem: 
  - Currently signer = account
    - in other words, we have problem 
      - Entire community relies on users being able to keep private key secret
          - users cannot make mistake
- Solution: 
  - Account abstraction !
    - Smart contract
      - Every account is now a smart contract that can have multiple rules
        - for instance 
          - multiple signers
          - different elliptic curves
          - 
    - Actually been on the roadmap since the beginning
    - https://eips.ethereum.org/EIPS/eip-4337

# updates-on-proposer-builder-separation
- mev-geth in POW
  - Searchers submits bundles to block producers
  - Bundles are scored, merged, and included by block producers
- PBS: mev -boost
  - Bidding 
    - Builders send full block bid into relay
    - Relay validates bids
  - Proposers
    - Proposers receives bids from relay
    - Proposers signs bid, and can no longer make another block
  - Delivery
    - Relay receives signed bid
- PBS separation
  - Market structure
    - Duties proposers cannot do
    - Proposers builder separation
      - The proposer outsources block construction to third party
  - An allocation mechanism
    - Whole block auction
      - Proposer sells off their right to make a block
      - 
  - https://ethresear.ch/t/unbundling-pbs-towards-protocol-enforced-proposer-commitments-pepc/13879?u=barnabe

# ultra-sound-money
- Ethereum as a company
  - profits = income - expenses
            = blockspace sales - security budget
            = burn - insurance
# towards-fairer-dexs-on-ethereum
- Market need 3 things to function
  - Thickness
    - Need a big enough supply of buyers and sellers
  - Safety
    - Participants should act truthfully reveal their preference
  - Overcome congestion
    - Give market participants means to make satisfiers choices when faced with multiple options
- On-chain order books
  - Etherdelta (RIP!)
  -> Hard to create thick markets 
    - Because it requirers a lot of management
- AMM
  - Uniswap, curve, etc
  - Solved problem of thick markets
  - Problem: MEV
  - Prices that depend on block ordering = unsafe
    - Solution: One price per block
- Batch auction step by step
  -  Users express trade intent (approval + signed message)
  -  On-chain liquidity + intent = thick market
  -  Settlement without ordering
     -  Uniform price clearing
     -   Solver competition to ensure best price
         -   Permissionsless competition
         -   Best solution gets the reward

# tackling-rounding-errors-with-precision-analysis
- https://osec.io/blog/reports/2022-04-26-spl-swap-rounding/
  - Rounding error
- Fuzzing + symbolic execution = solution


