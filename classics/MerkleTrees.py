import hashlib

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.hash = hashlib.sha256(str(value).encode()).hexdigest()
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return self.__str__()

    def merge(self, node):
        return Node(self.hash + node.hash)

class MerkleTree:
    def __init__(self, node_type=Node, empty_node=Node("")) -> None:
        self.node_type = node_type
        self.empty_node = empty_node

    def construct_tree(self, data_or_nodes):
        self.tree = self.hash(data_or_nodes)
        self.root = self.tree[-1]
        return self

    def hash(self, data_or_nodes):            
        encoded = []
        for i in data_or_nodes:
            if isinstance(i, self.node_type):
                encoded.append(i)
            else:
                encoded.append(self.node_type(i))

        if len(encoded) == 1:
            return encoded

        if len(data_or_nodes) % 2 != 0:
            # Padding
            encoded.append(self.empty_node)
        i = 0
        print(encoded[i].merge(encoded[i + 1]))

        return [encoded] +\
                self.hash([
                    encoded[i].merge(encoded[i + 1])
                     for i in range(0, len(data_or_nodes), 2)
                ])

if __name__ == "__main__":
    tree = MerkleTree().construct_tree(
        [1, 2, 3, 4]
    )
    tree_modified = MerkleTree().construct_tree(
        [1, 2, 3, 5]
    )
    for v in tree.tree:
        print(v)

    assert (tree.root) != tree_modified.root
