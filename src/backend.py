from bst import *

def create_tree(arr):
    tree = BST()

    for num in arr:
        tree.insert(num)

    return tree