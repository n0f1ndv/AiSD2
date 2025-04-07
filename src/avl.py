from nodes import Node_AVL
from traversals import findmin

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
    pivot=len(lst)//2
    root=Node_AVL(lst[pivot])
    if len(lst)!= 1:
        root.left=create_avl(lst[:pivot])
        root.right=create_avl(lst[pivot+1:])
    
    root.height = root.height = 1 + max(get_height(root.left), get_height(root.right))

    return root

def delete_avl(root, key):
    
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
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

        root.right = delete_avl(root.right, temp.key)
    
    if root is None:
        return root
        
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    
    if balance <-1 and get_balance(root.right) <= 0:
        return rotation_left(root)
    if balance <-1 and get_balance(root.right) > 0:
        root.right=rotation_right(root.right)
        return rotation_left(root)    
    if balance >1 and get_balance(root.left) < 0:
        root.left=rotation_left(root.left)
        return rotation_right(root)
    if balance >1 and get_balance(root.left) >= 0: 
        return rotation_right(root)

    return root

# TODO: delete operations and rebalance?? idk if it makes sense