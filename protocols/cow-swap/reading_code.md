# https://github.com/fleupold/dappcon-2022-smart-orders
- GPv2Order
  - https://eips.ethereum.org/EIPS/eip-712
    - Sign message with given structure
- GATOrders.sol
  - Data structure for an order
    - fields expected in a market order (valid from to, amount, tokens, etc)
  - Order placements
    - Tokens transferred from msg.sender to an GatOrder
- Sadly no mentions of how the relayers work 
  - Looks like it might be this https://eprint.iacr.org/2022/1066.pdf
    - Every transaction sent to the blockchain is first encrypted by the global public key
      - Comities of validators holds the private key
        - Only after a block is finalized it can be decrypted
          - i.e there is no information leakage
      - Uses https://en.wikipedia.org/wiki/Distributed_key_generation to create a keypair for the relayer pools
      - 

# https://github.com/cowprotocol/services
- orderbook
- autopilot
- solver
- +++
- 
# https://github.com/cowprotocol/contracts
