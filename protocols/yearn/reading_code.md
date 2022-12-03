Read https://github.com/yearn/yearn-protocol

contracts/
    controllers/
        controller.sol
            - Set strategies, vaults, etc
            - Calculates expected returns
            - earn
              - With a converter function, kinda cool actually to allow users to deposits anything
              - Deposits into strategy
            - yearn 
              - Withdraw token from strategy
              - what is one split ?
                - Some kind of distributions addr ?
                - No looks like it might be 1inch
                - https://github.com/1inch/1inchProtocol/blob/master/contracts/OneSplitAudit.sol
              - basically reinvestest non critical strategy tokens into strategy
              - cool idea!
        DelegatedController.sol
            - Same ideas as `controller.sol`
    exploits/EvilGauge.sol
        - `ERC20` token
    registries/YRegistry.sol
        - Trackers of controllers, strategy, etc
    strategies/
        - Various strategies
          - Again none of the interface ... for some reason
        - StrategyTUSDCurve.sol
          - Deposits
            - Takes true usd
            - Deposits into a yearn true usd contract address that is hard coded
              - https://etherscan.io/address/0x73a052500105205d34Daf004eAb301916DA8190f#code
            - Also add new liquidity if available
          - withdraw (asset)
            - Any asset not used by the strategy (tusd or curve related)
          - withdraw (amount)
            -  allows you to withdraw some true usd
          - Withdraw all
            - Withdraw all funds
          -   
    vaults/
        - Various vaults
          - But none of them implements the IVault interface ???
          - Did a quick pass over the files, and seems to be basically contract for giving "shares"
        - 


