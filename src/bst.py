class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.root
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
    
        return node

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

    def find_min(self, node):
        while node.left is not None:
            node = node.left

        return node

    def delete(self, key):
        current = self.root
        parent = None

        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

            if current is None:
                return
            
            # Node has no children
            if current.left is None and current.right is None:
                if current == self.root:
                    self.root = None
                elif current == parent.left:
                    parent.left = None
                else:
                    parent.right = None

            # Node has one child
            elif current.left is None or current.right is None:
                child = current.left if current.left is not None else current.right
                if current == self.root:
                    self.root = child
                elif current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            
            # Node has two children
            else:
                successor = self.find_min(current.right)
                successor_key = successor.key
                self.delete(successor_key)
                current.key = successor_key

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')