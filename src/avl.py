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


def create_avl(lst):
    if not lst:
        return None
    
    lst.sort()
    pivot = len(lst)//2
    root = Node_AVL(lst[pivot])
    if len(lst)!= 1:
        root.left=create_avl(lst[:pivot])
        root.right=create_avl(lst[pivot+1:])
    
    root.height = root.height = 1 + max(get_height(root.left), get_height(root.right))

    return root