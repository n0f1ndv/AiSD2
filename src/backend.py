from bst import *

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
    print(f'Min: {findmin_bst(tree).key}')
    print(f'Max: {findmax_bst(tree).key}')


def print_tree(tree):
    print('In-order:', end=' ')
    inorder_bst(tree)
    print()

    print('Pre-order:', end=' ')
    preorder_bst(tree)
    print()

    print('Post-order:', end=' ')
    postorder_bst(tree)
    print()


def delete_elements(tree):
    to_del = [int(x) for x in input('delete> ').split()]

    for num in to_del:
        tree = delete_bst(tree, num)

    return tree

def rebalance(tree, size):
    tree_to_vine_bst(tree)
    inorder_bst(tree)
    print()
    
    vine_to_tree_bst(tree, size)
    inorder_bst(tree)
    print()