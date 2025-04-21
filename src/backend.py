from bst import create_bst
from avl import create_avl
from traversals import *
from delete import delete
import time

def create_tree(lst, type):
    print(f'Inserting...', end=' ')
    for num in lst:
        print(f'{num}', end=' ')
    print()

    if type == 'BST':    
        root = create_bst(lst)
    elif type == 'AVL':
        root = create_avl(lst)

    return root


def help_message():
    print('Help Show this menu',
    'FindMinMax Searching minimum and maximum value in the tree (fmm for short)',
    'Print      Print the tree using In-order, Pre-order, Post-order',
    'Delete     Delete elements from the tree',
    'Delete All Delete whole tree',
    'Export     Export the tree to a file',
    'Rebalance  Rebalance the tree (BST only)',
    'Exit       Exits the program (same as CTRL+D)', sep='\n')


def findminmax(tree):
    print(f'Min: {findmin(tree).key}')
    print(f'Max: {findmax(tree).key}')


def print_tree(tree,b,type,size,input_type):
    if not b["print"]:
        print('In-order:', end=' ')
        inorder(tree)
        print()
    else:
        start = time.time()
        print('In-order:', end=' ')
        inorder(tree)
        print()
        stop = time.time()
        elapsed_time = round(stop - start, 4)
        print(elapsed_time)

        with open(f'benchmark_results/{type}/print_{input_type}.csv', 'a') as file:
            file.write(f"print,{elapsed_time},{size}\n")


    print('Pre-order:', end=' ')
    preorder(tree)
    print()

    print('Post-order:', end=' ')
    postorder(tree)
    print()


def delete_elements(tree):
    try:
        to_del = [int(x) for x in input('delete> ').replace(","," ").split()]
        for num in to_del:    
            tree = delete(tree, num)
    except ValueError:
        print('Error: Invalid integer')

    return tree


def export(root, file):
    file.write(f"{{{root.key}}}\n")
    file.write("child ")
    if root.left is None:
        file.write("[missing]\n")
    else:
        file.write("{node\n")
        export(root.left, file)
        file.write("}\n")

    file.write("child ")
    if root.right is None:
        file.write("[missing]\n")
    else:
        file.write("{node\n")
        export(root.right, file)
        file.write("}\n")