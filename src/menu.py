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

def delete(tree):
    to_del = [int(x) for x in input('delete> ').split()]

    for num in to_del:
        tree.remove(num)

def menu(arr):
    state = ''

    tree = Node(arr[0])
    create_tree(tree, arr[1:])

    print(f'Inserting...', end=' ')
    for num in arr:
        print(num, end=' ')
    print()

    while True and state != 'exit':
        state = input('action> ').strip().lower()

        if state == 'help':
            help_message()
        elif state == 'findminmax' or state == 'fmm':
            findminmax(tree)
        elif state == 'print':
            print_tree(tree)
        elif state == 'delete':
            delete(tree)
        elif state == 'delete all':
            tree.delete_tree(tree.root)
            print('Tree succesfully removed')
        elif state == 'export':
            pass # This is for extra points I will do it later
        elif state == 'rebalance':
            pass
        elif state == 'exit':
            state = 'exit'