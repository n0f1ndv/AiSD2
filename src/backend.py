from bst import *
from avl import *
from traversals import *
from delete import *

def create_tree(lst, type):
    print(f'Inserting...', end=' ')
    for num in lst:
        print(f'{num}', end=' ')
    print()

    if type == 'BST':    
        root = create_bst(lst)
    elif type == 'AVL':
        root = create_avl(lst)

    return root


def help_message():
    print('Help Show this menu',
    'FindMinMax Searching minimum and maximum value in the tree (fmm for short)',
    'Print      Print the tree using In-order, Pre-order, Post-order',
    'Delete     Delete elements from the tree',
    'Delete All Delete whole tree',
    'Export     Export the tree to a file',
    'Rebalance  Rebalance the tree (BST only)',
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


def delete_elements(tree):
    to_del = [int(x) for x in input('delete> ').split()]

    for num in to_del:    
        tree = delete(tree, num)

    return tree


def export(root, file):
    file.write(f"{{{root.key}}}\n")
    file.write("child ")
    if root.left is None:
        file.write("[missing]\n")
    else:
        file.write("{node\n")
        export(root.left, file)
        file.write("}\n")

    file.write("child ")
    if root.right is None:
        file.write("[missing]\n")
    else:
        file.write("{node\n")
        export(root.right, file)
        file.write("}\n")