[https://a16zcrypto.com/hidden-in-plain-sight-a-sneaky-solidity-implementation-of-a-sealed-bid-auction/](https://a16zcrypto.com/hidden-in-plain-sight-a-sneaky-solidity-implementation-of-a-sealed-bid-auction/)

- Commit -> Reveal scheme
  - Use `CREATE2` with constructor parameters encoding the bid and auction id in a vault design
  - Bidders can send ETH to the vault before it's deployed
  - `SneakyVaults`
    - Unlocks the vaults
  - This makes it all look like normal transfers
  - 
- 






