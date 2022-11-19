from MerkleTrees import MerkleTree, Node

def verify():
    """
                E
            /       \ 
        C            D
       /\
     A    B        
    """

    """
    We submit B
    -> Service give us root hash
    -> Want to verify that B is included.
    -> We request hash of A, D
    """
    tree = MerkleTree().construct_tree(
        [1, 2, 3]
    )
    root_hash = tree
    hash_a = Node(1)
    hash_d = Node(3)

    re_constructed_tree = MerkleTree().construct_tree(
        [hash_a, 2, hash_d]
    )
    assert str(root_hash.root) == str(re_constructed_tree.root)

def consistency():
    """
                E
            /       \ 
        C            D
       /\           /
     A    B        E
    """

    """
    We add new node E
    -> Want to verify against old tree

    -> Verify that new tree with all data without E give same root hash
    -> Add E to old tree and verify it gives same hash as new tree
    """
    


if __name__ == "__main__":
    verify()
    consistency()
