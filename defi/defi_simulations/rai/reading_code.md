
https://github.com/reflexer-labs/geb

single/
    AccountingEngine.sol
    - Debt is pushed into queues
    - Debt that is not in a queue or in a auction can be deleted
    - Debt auctions

    CoinSavingsAccount.sol
    - Let's you get interest on protocol token
    
    CollateralAuctionHouse.sol
    - EnglishCollateralAuctionHouse
        - Includes old name (?) EnglishCollateralAuctionHouse.sol
        - No, it just has many different types of auctions
        - Let's you auction out Collateral for system coins
    - FixedDiscountCollateralAuctionHouse
        - Let's you sell some collateral at a fixed discount in order to instantly recapitalize the system
    - IncreasingDiscountCollateralAuctionHouse.sol
        - This allows you to sell some collateral at an increasing discount

    - DebtAuctionHouse
      - 