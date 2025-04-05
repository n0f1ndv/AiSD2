class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    tmp = Node(key)

    if root is None:
        return tmp
    
    parent = None
    current = root
    while current is not None:
        parent = current
        #print(f'key ... current.key: {key} ... {current.key}')
        if key < current.key:
            current = current.left
        elif key > current.key:
            current = current.right
        else:
            return root # key already exists
        
    if key < parent.key:
        parent.left = tmp
        #print(f'par {parent.key}')
    else:
        parent.right = tmp
        #print(f'par {parent.key}')

    return root

def create_tree(root, lst):
    for num in lst:
        root = insert(root, num)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')

def findmin(node):
    while node.left is not None:
        node = node.left

    return node
    
def findmax(node):
    while node.right is not None:
        node = node.right

    return node