from backend import create_tree

def help_message():
    print('Help Show this menu',
    'Print      Print the tree using In-order, Pre-order, Post-order',
    'Remove     Remove elements from the tree',
    'Delete     Delete whole tree',
    'Export     Export the tree to a file', # Maybe I will do it I dunno
    'Rebalance  Rebalance the tree',
    'Exit       Exits the program (same as CTRL+D)', sep='\n')


def print_tree(tree):
    print('In-order:', end=' ')
    tree.inorder(tree.root)
    print()
    print('Pre-order:', end=' ')
    tree.preorder(tree.root)
    print()
    print('Post-order:', end=' ')
    tree.postorder(tree.root)
    print()


def menu(arr):
    state = ''
    tree = create_tree(arr)

    print(f'nodes> ')
    print(f'insert> ')

    while True and state != 'exit':
        state = input('action> ')

        if state.lower() == 'help':
            help_message()
        elif state.lower() == 'print':
            print_tree(tree)
        elif state.lower() == 'remove':
            pass
        elif state.lower() == 'export':
            pass
        elif state.lower() == 'rebalance':
            pass
        elif state.lower() == 'exit':
            state = 'exit'