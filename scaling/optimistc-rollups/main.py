from L1 import Layer1
from L2 import Layer2
from Sequencer import Sequencer

if __name__ == "__main__":
    layer1 = Layer1()
    layer2 = Layer2()
    
    sequencer = Sequencer()
    # User deposit 10 eth into layer 1 smart contract
    layer1.deposit(
        10, 
        "user a"
    )
    # reads deposit from l1 and move into l2
    sequencer.process()
    """
    User can now freely work in the l2 env
    """

    """
    Okay, so what is so special about this ? Seem like a normal bridge ?

    We do state updates of the l2 into the l1
    Contract on l1 stores merkle root of the rollup state (l2)
    -> I.e state balance and evm 

    Sequence submissions to the l1 contain a pre-state and post-state
    -> Basically like a traditional block chain
    -> It also publish the transaction data from the l2 onto the layer 1
        -> Without the execution (of courses)
    
    The challenges with L2 are mostly around fraud proofs
    -> Sequencer should not do anything illegal!
        -> How to prove this ? 
            -> Challengers will challenge some batch update
                ->  Transaction x is in valid 
                    -> Can then be proved again on L1 
                        -> If challangers proof is correct then the invalid batch is reverted
    
    """
    