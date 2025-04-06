from nodes import Node_AVL

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
    tmp = Node_AVL(key)

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

# TODO: delete operations and rebalance?? idk if it makes sense