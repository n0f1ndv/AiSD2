from backend import *
from datetime import datetime
import sys

def menu(lst, type,):
    state = ''
    tree = create_tree(lst, type)

    #sys.stdin = open('/dev/tty')
    while True and state != 'exit':
               
        try:
            state = input('action> ').strip().lower()

            if state == 'help':
                help_message()

            elif state == 'findminmax' or state == 'fmm':
                findminmax(tree)

            elif state == 'print':
                print_tree(tree)

            elif state == 'delete':
                tree = delete_elements(tree)

            elif state == 'delete all':
                tree = delete_all(tree)

            elif state == 'export':
                with open(f'../data/exported{datetime.now().strftime('%H%M%S')}.txt', 'w') as file:
                    export(tree, file)
                print('Exporting')

            elif state == 'rebalance':
                if type == 'BST':
                    tree = vine_to_bst(tree)
                else:
                    print('This operation is only avaiable for BST')

            elif state == 'exit':
                print('Closing the program')
                state = 'exit'

        except EOFError:
            state = 'exit'
            print('\nEnd of input detected. Exiting program.')
            
        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')