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
            tree = delete_elements(tree) # BST specific waiting for AVL impl
        elif state == 'delete all':
            tree = delete_all_bst(tree) # BST specific ^ same 
        elif state == 'export':
            pass # This is for extra points I will do it later
        elif state == 'rebalance':
            tree = vine_to_bst(tree) # BST specific
        elif state == 'exit':
            print('Closing the program')
            state = 'exit'