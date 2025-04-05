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


def menu(arr):
    state = ''

    tree = create_tree(arr)

    while True and state != 'exit':
        state = input('action> ').strip().lower()

        if state == 'help':
            help_message()
        elif state == 'findminmax' or state == 'fmm':
            findminmax(tree)
        elif state == 'print':
            print_tree(tree)
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