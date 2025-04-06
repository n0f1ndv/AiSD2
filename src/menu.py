from backend import *

def menu(lst, type):
    state = ''
    tree = create_tree(lst, type)

    while True and state != 'exit':
        try:
            state = input('action> ').strip().lower()
        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')

        if state == 'help':
            help_message()
        elif state == 'findminmax' or state == 'fmm':
            findminmax(tree)
        elif state == 'print':
            print_tree(tree)
        elif state == 'delete':
            if type == 'BST':
                tree = delete_elements(tree, type) # BST specific waiting for AVL impl
            elif type == 'AVL':
                pass # TODO Put delete function here
        elif state == 'delete all':
            if type == 'BST':
                tree = delete_all_bst(tree)
            elif type == 'AVL':
                # tree = delete_all_avl(tree)
                pass # TODO Put delete all function here
        elif state == 'export':
            pass # This is for extra points I will do it later
        elif state == 'rebalance':
            tree = vine_to_bst(tree) # BST specific
        elif state == 'exit':
            print('Closing the program')
            state = 'exit'