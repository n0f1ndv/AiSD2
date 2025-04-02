from menu import menu
from bst import *

def main():
    tree = BST()

    # TODO: create a function to create tree
    tree.insert(20)
    tree.insert(14)
    tree.insert(3)
    tree.insert(11)
    tree.insert(27)
    tree.insert(8)

    menu(tree)

if __name__ == "__main__":
    main()