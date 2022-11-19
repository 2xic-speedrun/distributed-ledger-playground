"""
https://ethereum.org/en/developers/docs/scaling/plasma/

-> Plasma is built on top of other chains 
-> Merkle proofs are used to do state commitments to the l1
-> Uses a smart contract to store state commiments, adn handle the moving of funds 
    -> The plasma operator looks for deposits and credits the users on plasma chain
    -> Withdrawing requirers "proof of funds"
        -> Various approaches
    -> Fraud proofs are also here used
-> Problems with plasma
    -> data is not stored on chain
        -> fraud proofs requirers that block producers are cooperative
        
"""