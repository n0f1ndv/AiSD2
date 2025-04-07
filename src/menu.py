from backend import *
import sys
def menu(lst, type,):
    state = ''
    tree = create_tree(lst, type)

    while True and state != 'exit':
               
        try:
            state = input('action> ').strip().lower()
        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')
        except EOFError:
            state = 'exit'
            print("\nEnd of input detected. Exiting program.")

        if state == 'help':
            help_message()
        elif state == 'findminmax' or state == 'fmm':
            findminmax(tree)
        elif state == 'print':
            print_tree(tree)
        elif state == 'delete':
            tree = delete_elements(tree, type)
        elif state == 'delete all':
            if type == 'BST':
                tree = delete_all_bst(tree)
            elif type == 'AVL':
                # tree = delete_all_avl(tree)
                pass # TODO Put delete all function here
        elif state == 'export':
            with open("exported.txt", "w") as file:
                export(tree, file) # TODO: minimal improvements
            print("exporting")
        elif state == 'rebalance':
            tree = vine_to_bst(tree) # BST specific
        elif state == 'exit':
            print('Closing the program')
            state = 'exit'