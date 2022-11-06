# Notes from the paper "Casper the friendly gadget"
[Paper](https://arxiv.org/pdf/1710.09437.pdf)


## introduction
- Chain-based proof of stake 
  - Design used in i.e peercoin
  - Mimics proof of work in some regards by pseudo-randomly selecting some to "mine" the next block
- Byzantine fault tolerant proof of stake
  - Tendermint started with this kind of design
  - Can (usually) be proofed to have certain properties mathematically

## What is casper ? 
- Casper is an overlay on top of a proposal mechanism
- That means even if an attacker control's the proposal mechanism, casper won't finalize the blocks if it's not compatible with current chain

Some features casper introduces
- accountability
  - if a validator violates a rule, we know who to "punish"
- Dynamic validators
  - validators can change over time
- Safety
  - 2/3 of the network is all that is needed to stay honest
- Modular design 
  - easy to add to existing proof of work chain

### The protocol
- First version is a hybrid PoW / PoS system
  - Future version could be some kind of round-robin block signing scheme
- Under normal circumstances blocks will come in a ordered way
  - each parent has exactly one child block
    - However, if there is latency's or attacks then the network might have multiple blocks with the same parent.
      - Caspers job is to then select the next block  
- Casper deals with checkpoints instead of the full block history
  - Checkpoint is the genesis block
  - Every block with a height that is a multiple of 100 is also a checkpoint
  
Notation


| Notation | Description                                       |
| -------- | ------------------------------------------------- |
| s        | The hash of any justified checkpoint              |
| t        | Any checkpoint hash that is decedent of s         |
| h(s)     | The height of checkpoint s in the checkpoint tree |
| h(t)     | The height of checkpoint t in the checkpoint tree |
| S        | signature of <s t, h(s), h(t)>> from validator v  |

From this we also have
- *Supermajority link* is a checkpoint pair a -> b such that at least 2/3 of validators (by deposit) have voted a as source, and b as target
  - Supermajority links can skip checkpoints, i.e this is an valid statement h(a) + 1 < h(b)
- *a* and *b* are in conflicting if they are not from the same branch
- checkpoint *c* is justified if 
  - it is the root
  - there is a supermajority link c' where checkpoint c' is justified
- checkpoint *c* is finalized if 
  - is is the root
  - it is justified and there is a supermajority link c -> c' where c' is a direct child of *c* 
    - iif *c* is justified.
  
### Rules
- Validator can not publish two distinct votes on same block height
- Cannot vote in the span of it's other votes

## Section 2.1 - proving the safety and plausible liveness
- see page 4

## Dynamic validator sets
- To deposit money they send a deposit message
  - 
- To withdraw you have to send a withdraw message
  - Then the money is put in a withdraw state
    - BUT if you violate the rules during this state, the money is slashed
    - The public key is also forbidden to rejoin the validation set during this period

## Dealing with offline nodes
- Nodes that are offline pay a fee for not voting.
  - They will the users who are voting will slowly become the majority.
  -  