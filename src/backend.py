from bst import *
from avl import *
from traversals import *

def create_tree(lst, type):
    print(f'Inserting...', end=' ')
    for num in lst:
        print(f'{num}', end=' ')
    print()

    root = Node(lst[0])
    for num in lst[1:]:
        if type == 'BST':
            root = insert_bst(root, num)
        elif type == 'AVL':
            root = insert_avl(root, num)

    return root


def help_message():
    print('Help Show this menu',
    'FindMinMax Searching minimum and maximum value in the tree',
    'Print      Print the tree using In-order, Pre-order, Post-order',
    'Delete     Delete elements from the tree',
    'Delete All Delete whole tree',
    'Export     Export the tree to a file',
    'Rebalance  Rebalance the tree',
    'Exit       Exits the program (same as CTRL+D)', sep='\n')


def findminmax(tree):
    print(f'Min: {findmin(tree).key}')
    print(f'Max: {findmax(tree).key}')


def print_tree(tree):
    print('In-order:', end=' ')
    inorder(tree)
    print()

    print('Pre-order:', end=' ')
    preorder(tree)
    print()

    print('Post-order:', end=' ')
    postorder(tree)
    print()


def delete_elements(tree, type):
    to_del = [int(x) for x in input('delete> ').split()]

    for num in to_del:
        if type == 'BST':
            tree = delete_bst(tree, num)
        elif type == 'AVL':
            # tree = delete_avl(tree, num)
            pass

    return tree