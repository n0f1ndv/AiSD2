from backend import *
import sys
def menu(lst, type,):
    state = ''
    tree = create_tree(lst, type)
    sys.stdin = open('/dev/tty')
    while True and state != 'exit':
               
        try:
            state = input('action> ').strip().lower()
        except EOFError:
            state = 'exit'
            print("\nEnd of input detected. Exiting program.")
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
            try:
                tree = delete_elements(tree, type)
            except ValueError:
                print("Error: Invalid integer")
            except KeyboardInterrupt:
                state = 'exit'
                print('\nKeyboard Interrupt') 
        elif state == 'delete all':
            if type == 'BST':
                tree = delete_all_bst(tree)
            elif type == 'AVL':
                # tree = delete_all_avl(tree)
                pass # TODO Put delete all function here
        elif state == 'export':
            with open("exported.txt", "w") as file:
                export(tree,file)
            print("exporting")
        elif state == 'rebalance':
            tree = vine_to_bst(tree) # BST specific
        elif state == 'exit':
            print('Closing the program')
            state = 'exit'