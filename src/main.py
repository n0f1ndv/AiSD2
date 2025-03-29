from menu import *
from bst import *


def main():
    tree = BST()

    tree.insert(20)
    tree.insert(14)
    tree.insert(3)
    tree.insert(11)
    tree.insert(27)
    tree.insert(8)

    tree.inorder(tree.root)

if __name__ == "__main__":
    main()