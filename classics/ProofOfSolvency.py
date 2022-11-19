from MerkleTrees import MerkleTree, Node
import hashlib
# Based on the idea from
# https://vitalik.ca/general/2022/11/19/proof_of_solvency.html


class UserBalance(Node):
    def __init__(self, name, balance) -> None:
        super(Node).__init__(Node)

        self.metadata = hashlib.sha256(f"{name}{balance}".encode()).hexdigest()
        self.balance = balance
        self.value = self.metadata
    
    def merge(self, node):
        return UserBalance(
            "LR",
            self.balance + node.balance,
        )

class BalanceTree(MerkleTree):
    def __init__(self) -> None:
        super().__init__(UserBalance, UserBalance("<>", 0))

if __name__ == "__main__":
    """
        You need to include the user balance
    """
    data = [
        UserBalance("Bob", 100),
        UserBalance("Carol", 200),
        UserBalance("David", 50),
    ]
    #data = list(map(str, data))
    proof_balance = BalanceTree().construct_tree(data)
    print("Balance ", proof_balance.root.balance)

    """
        Because else you can cheat like this!

        Where exchange only provide node hash! :o
    """
    data = [
        Node("Bob -100"),
        Node("Carol -200"),
        Node("David -50"),
    ]
    #data = list(map(str, data))
    proof_balance = MerkleTree().construct_tree(data)
    print("Balance ", proof_balance.root.hash)
