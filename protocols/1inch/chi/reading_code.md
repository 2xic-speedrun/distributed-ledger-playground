https://github.com/1inch/chi 

contracts/ChiToken.sol
    - ChiToken
        - ERC20
        - ERC20WithoutTotalSupply
      - mint    
        - Does an mstore starting at offset 0
        - runs create2 to create multiple contracts
          - Which is what creates the "supply"
            - because of the gas refund mechanism
          - offset is based on the total minted supply
          - i.e always expanding if nothing is burned
        - computeAddress2
          - 
        -  _destroyChildren
           -  Destroys the contracts
           -  