https://github.com/1inch/1inchProtocol


contracts/
    interface/*
        - So many
    BalanceHelper.sol
        - Get the returns for swaps between tokens
    BalancerLib.sol
        - Various math utils
    BancorFinder.sol
        - Find a valid path in bancor for from and dest token
    (I)OneSplit.sol
        - Multiple implementations for the logic needed to do swaps

        - getExpectedReturnWithGas
            -> super.getExpectedReturnWithGas
        - swap
            - swap logic
    UniversalERC20.sol
        - Cool, clean way to make ETH work neatly as an ERC20 (at least for transfers)
  


