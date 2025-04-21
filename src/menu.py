from backend import *
from bst import vine_to_bst
from delete import delete_all
from datetime import datetime
import sys
import time
def menu(lst, type, b):
    input_type=sys.stdin.readline().strip()
    size=len(lst)
    state = ''
    if b["create"]:
        start=time.time()
        tree = create_tree(lst, type)
        stop=time.time()
        elapsed_time = round(stop - start, 4)
        with open(f'benchmark_results/{type}/create_{input_type}.csv', 'a') as file:
            file.write(f"creation,{elapsed_time},{size}\n")
    else:
        tree = create_tree(lst, type)

    # sys.stdin = open('/dev/tty')        #used when normal usage
    while True and state != 'exit':
               
        try:
            state=sys.stdin.readline().strip()             #used when benchamarking from a txt file
            # state = input('action> ').strip().lower()    #used when normal usage 

            if state == 'help':
                help_message()

            elif state == 'findminmax' or state == 'fmm':
                if not b["findminmax"]:
                    findminmax(tree)
                else:
                    start = time.time()
                    findminmax(tree)
                    stop = time.time()
                    elapsed_time = round(stop - start, 4)
                    print(elapsed_time)
                    with open(f'benchmark_results/{type}/findminmax_{input_type}.csv', 'a') as file:
                        file.write(f"findminmax,{elapsed_time},{size}\n")

            elif state == 'print':
                print_tree(tree,b,type,size,input_type)

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
                    if not b["rebalance"]:
                        tree = vine_to_bst(tree)
                    else:
                        start = time.time()
                        tree = vine_to_bst(tree)
                        stop = time.time()
                        elapsed_time = round(stop - start, 4)
                        print(elapsed_time)
                        with open(f'benchmark_results/{type}/rebalance_{input_type}.csv', 'a') as file:
                            file.write(f"rebalance,{elapsed_time},{size}\n")
                else:
                    print('This operation is only avaiable for BST')

            elif state == 'exit':
                print('Closing the program')
                state = 'exit'
        except KeyboardInterrupt:
            state = 'exit'
            print('\nKeyboard Interrupt')