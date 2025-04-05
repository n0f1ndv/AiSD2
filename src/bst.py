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


def create_tree(lst):
    root = Node(lst[0])

    print(f'Inserting... {lst[0]}', end=' ')
    for num in lst[1:]:
        root = insert(root, num)
        print(num, end=' ')
    print()

    return root


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


def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = findmin(root.right)
        root.key = temp.key

        root.right = delete(root.right, temp.key)

    return root



def delete_all(root):
    pass