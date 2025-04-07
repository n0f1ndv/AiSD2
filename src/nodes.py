class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class Node_AVL(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1