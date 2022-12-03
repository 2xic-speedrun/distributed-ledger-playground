https://github.com/1inch/farming

contracts/
          accounting/
                    FarmAccounting.sol
                        farmingAccountIng.sol
                            - Returns amount reward since last checkpoint
                        startFarming
                            - Tracks the accounting, and returns the amount
                    UserAccounting.sol
                        farmedPerToken
                            - given a token return farmed per token stored
         interfaces/
                    Skipping this for now
         mocks/
                    Skipping this for now
         FarmingLib.sol
            makeInfo
              - create info struct
            getDate
                - create data slot
            startFarming
                - Updates the user accounting based on input amount and period
            farmed
                Get how much you have farmed
            claim   
                Updated the accounting to adjust for the balance
            farmedPerToken
                same as in user accounting
         FarmingPod.sol
            totalSupply
                - of the farm
            getFarmInfo
                - info of the farm
            setDistributor
                - person allow to rescue funds, and start farming
            startFarming
                - Move the rewards tokens to the address, and starts the farming
            claim
                - If you have balance you cna claim reward token
         FarmingPool.sol
            More or less same logic here as in FarmingPod.sol

            - Supports deposits, withdraw
            - 
         MultiFarmingPod.sol
            Allows multiple farms to be farming!!
