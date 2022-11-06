# Notes from the paper "Proof of Stake Made Simple with Casper"
[Paper](https://www.scs.stanford.edu/17au-cs244b/labs/projects/moindrot_bournhonesque.pdf)

- They implemented a simple version of casper https://github.com/omoindrot/simple_casper
- Casper guarantees Byzantine Fault Tolerance of up to 1/3 of validators
- Casper requirers that validators vote (cryptographically signed), and publish them to the other validators.
    - Earlier versions of the protocol followed a prepare, and commit message
    - Current version only has a single message type
- Block finality in Casper happens when 2/3 validators follows a block.
- Votes are proportional to users stake amount
  - Validators will try to agree on a checkpoint every 100 blocks.
    - In exchange for this, they receive a small reward to incentives good behavior.

- Validation
    - If 2/3 of validators cast a vote on c' as a source, and c as a target then this is a super-majority link.
      - Fancy word for that they agree on link
    - Justified checkpoint
      - if it is the genesis block
      - if there is a super-majority link c' -> c where c' is justified (recursive)
    - Finalized checkpoint
      - checkpoint c is finalized if it is justified and there is a super-majority link c -> c' 
        - c' has to be a direct child of c
- Slashing
  - Two rules
    - Cannot publish two distinct votes on the same height
    - a validator must not vote within the span of it's other votes.
  - Deposit is destroyed (slashed) if those rules are broken

- 
