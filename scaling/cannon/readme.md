cannon cannon cannon!

----
While being kinda familiar with the optimism stack, I was still unsure how the fault proof worked (I had kinda looked at cannon before, but not deep).

I guess this makes sense, by reconstructing the merkle trie, and verifying it with geth you don't need to worry much.


----

contracts/lib
    - Mostly helper functions for 
      - binary operators
      - sha3
      - MerkelTrie
      - RLP RW 
contracts/Challenge
    - Mips computer
    - State
      - L
      - R
      - Asserted state
      - Defended state
    -  Create challenge
       -  Set the state
          -  StartState
          -  final state 
          - L and R (Left and right for binary search)
        - Internal function called from InitiateChallenge
     - CallWithTrieNodes
       - Calls an contract with data
     - InitiateChallenge
        - Prepare the MIPS machine for the challenge
        - With verifications checks of input
      - RespondState + ProposedState
        - Communication between challenger and owner
        - Proposing various states
          - If agree on state move forward
          - Else move backward
          - Starts at middle state, and preforms binary search to find disagreement
      - When search is finished
        - ConfirmStateTransition
        - If not searching anymore
          - Run the asserted state in the mips machine
            - and payout if the state is not as asserted
contracts/mips
    - WriteMemory
    - RedMemory
    - Steps
      - Move the program counter
      - Fetches new state hash
    - StepPC
      - Updates state
    - execute
      - Opcodes definition
contracts/Mips-memory
    - PreImage
      - https://medium.com/ethereum-optimism/cannon-cannon-cannon-introducing-cannon-4ce0d9245a03
      - preimage oracle
        - "Oracle" is a loose term here, but okay
      - https://twitter.com/ben_chain/status/1488275963360120832
      - https://github.com/ethereum-optimism/cannon/wiki/Cannon-Overview#minigeth-gnarly-details
      - RPC calls could also be used to get value from GETH (not how it's done in minigeth)
        - PrefetchAccount
        - PrefetchStorage
        - PrefetchCode
        - PrefetchBlock
      - Oh wait, I think I now see why this is so cool
        - Since both hashes in l1, and l2 is relevant
        - You need a way to provide not only the l1 hash, but also the l2
        - block -> hash(block) -> block.hash
          ^------- oracle preimage <---- v

---
geth -> Compiles to mips and executed
---
scripts/
    - assert
      - Verify that state transition is working
    - Challenge
      - Initiate the challenge
    - Deploy
      - Deploys
    - lib
      - Helper functions
      - Various helper functions
    - Respond
      - Verify the responder




