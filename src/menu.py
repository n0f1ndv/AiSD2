from backend import *

def menu(lst):
    state = ''
    tree = create_bst(lst)

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
            tree = delete_elements(tree)
        elif state == 'delete all':
            tree = delete_all_bst(tree)
        elif state == 'export':
            pass # This is for extra points I will do it later
        elif state == 'rebalance':
            tree = vine_to_bst(tree)
        elif state == 'exit':
            print('Closing the program')
            state = 'exit'