import math
from nodes import Node

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


def create_bst(lst):
    root = Node(lst[0])

    for num in lst[1:]:
        root = insert_bst(root, num)

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