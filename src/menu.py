from backend import create_tree

def help_message():
    print('Help Show this menu',
    'Print      Print the tree using In-order, Pre-order, Post-order',
    'Delete     Delete elements from the tree',
    'Delete All Delete whole tree',
    'Export     Export the tree to a file',
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


def delete(tree):
    to_del = [int(x) for x in input('delete> ').split()]

    for num in to_del:
        tree.remove(num)


def menu(arr):
    state = ''
    tree = create_tree(arr)

    print(f'nodes> {len(arr)}')
    print(f'insert> {arr}')

    while True and state != 'exit':
        state = input('action> ').strip().lower()

        if state == 'help':
            help_message()
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