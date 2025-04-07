import math
from nodes import Node
from traversals import findmin

# INSERTING ELEMENTS INTO BST
def insert_bst(root, key):
    tmp = Node(key)

    if root is None:
        return tmp
    
    parent = None
    current = root
    while current is not None:
        parent = current
        if key < current.key:
            current = current.left
        elif key > current.key:
            current = current.right
        else:
            return root
        
    if key < parent.key:
        parent.left = tmp
    else:
        parent.right = tmp

    return root


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
        
        temp = findmin(root.right)
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
def bst_to_vine(root):
    count = 0
    
    tmp = root.right
    while tmp:
        if tmp.left:
            old_tmp = tmp
            tmp = tmp.left
            old_tmp.left = tmp.right
            tmp.right = old_tmp
            root.right = tmp
        else:
            count += 1
            root = tmp
            tmp = tmp.right

    return count


def vine_to_bst(root):
    grand = Node(0)

    grand.right = root

    count = bst_to_vine(grand)

    height = int(math.log2(count + 1))

    nodes = pow(2, height) - 1

    compress(grand, count - nodes)

    for nodes in [nodes // 2**i for i in range(1, height + 1)]:
        compress(grand, nodes)

    return grand.right


def compress(root, count):
    tmp = root.right
 
    # Traverse and left-rotate root m times to compress given vine form of BST
    for i in range(count):
        oldTmp = tmp
        tmp = tmp.right
        root.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        root = tmp
        tmp = tmp.right