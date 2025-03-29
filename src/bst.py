class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
    
        return x

    def insert(self, key):
        new_node = Node(key)
        # If the tree is empty, set the new node as root
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self):
        pass

    def inorder(self):
        pass

    def preorder(self):
        pass
    
    def postorder(self):
        pass