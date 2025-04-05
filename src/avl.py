class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotation_left(x):
    y = x.right
    tmp = y.left
    y.left = x
    x.right = tmp
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def rotation_right(x):
    y = x.left
    tmp = y.right
    y.right = x
    x.left = tmp
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def insert_avl(root, key):
    tmp = Node(key)

    if root is None:
        return tmp
    
    if key < root.key:
        root.left = insert_avl(root.left,key)
    elif key > root.key:
        root.right = insert_avl(root.right,key)
    else:
        return root
        
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    balance = get_balance(root)
    if balance <-1 and key > root.right.key: #przeważa prawa gałąź, nowy liść po prawej stronie
        return rotation_left(root)
    if balance <-1 and key < root.right.key: #przeważa prawa gałąź, nowy liść po lewej stronie
        root.right=rotation_right(root.right)
        return rotation_left(root)    
    if balance >1 and key > root.left.key: #przeważa lewa gałąź, nowy liść po prawej stronie
        root.left=rotation_left(root.left)
        return rotation_right(root)
    if balance >1 and key < root.left.key: #przeważa lewa gałąź, nowy liść po lewej stronie
        return rotation_right(root)

    return root


def create_tree_avl(lst):
    root = Node(lst[0])

    print(f'Inserting... {lst[0]}', end=' ')
    for num in lst[1:]:
        root = insert_avl(root, num)
        print(num, end=' ')
    print()

    return root

#----------------------------------------------------------------------------------------------------------------

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
    pass


def delete_all(root):
    pass
def findminmax(tree):
    print(f'Min: {findmin(tree).key}')
    print(f'Max: {findmax(tree).key}')


def print_tree(tree,lst):
    print('In-order:', end=' ')
    inorder(tree,lst)
    print()

    print('Pre-order:', end=' ')
    preorder(tree)
    print()

    print('Post-order:', end=' ')
    postorder(tree)
    print()


def menu(arr):
    state = ''

    tree = create_tree_avl(arr)

    while True and state != 'exit':
        state = input('action> ').strip().lower()

        if state == 'findminmax' or state == 'fmm':
            findminmax(tree)
        elif state == 'print':
            print_tree(tree,lista)
        elif state == 'delete':
            pass
        elif state == 'delete all':
            pass
        elif state == 'export':
            pass # This is for extra points I will do it later
        elif state == 'rebalance':
            pass
        elif state == 'exit':
            state = 'exit'
menu([1,2,3,6,5,4,7])