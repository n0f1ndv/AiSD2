import math

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


# INSERTING ELEMENTS INTO BST
def insert_bst(root, key):
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


def create_bst(lst):
    print(f'Inserting...', end=' ')
    for num in lst:
        print(f'{num}', end=' ')
    print()

    root = Node(lst[0])
    for num in lst[1:]:
        root = insert_bst(root, num)

    return root


# TRAVERSING BST
def inorder_bst(node):
    if node:
        inorder_bst(node.left)
        print(node.key, end=' ')
        inorder_bst(node.right)


def preorder_bst(node):
    if node:
        print(node.key, end=' ')
        preorder_bst(node.left)
        preorder_bst(node.right)


def postorder_bst(node):
    if node:
        postorder_bst(node.left)
        postorder_bst(node.right)
        print(node.key, end=' ')


# FINDING MIN MAX IN BST
def findmin_bst(node):
    while node.left is not None:
        node = node.left

    return node
    

def findmax_bst(node):
    while node.right is not None:
        node = node.right

    return node


# DELETING FROM BST
def delete_bst(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = findmin_bst(root.right)
        root.key = temp.key

        root.right = delete_bst(root.right, temp.key)

    return root


def delete_all_bst(root):
    if root:
        delete_all_bst(root.left)
        delete_all_bst(root.right)
        root = None

    return root


# BALANCING BST
def tree_to_vine_bst(root):
    tail = root
    rest = tail.right
    while rest is not None:
        if rest.left is None:
            tail = rest
            rest = rest.right
        else:
            temp = rest.left
            rest.left = temp.right
            temp.right = rest
            rest = temp
            tail.right = temp


def vine_to_tree_bst(root, size):
    leaves = size + 1 - pow(2, math.floor(math.log2(size + 1)))
    compress(root, leaves)
    size -= leaves
    while size > 1:
        compress(root, math.floor(size / 2))
        size = math.floor(size / 2)


def compress(root, count):
    scanner = root
    for _ in range(count):
        child = scanner.right
        if child is None:
            break
        scanner.right = child.right
        child.right = scanner.right.left if scanner.right else None
        if scanner.right is not None:
            scanner.right.left = child
        scanner = scanner.right if scanner.right else scanner