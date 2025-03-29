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

    node = tree.search(27)
    print("Node found:", node.key if node else "Not found")

    node = tree.search(310)
    print("Node found:", node.key if node else "Not found")

    tree.delete(27)
    node = tree.search(27)
    print("Node found:", node.key if node else "Not found")

if __name__ == "__main__":
    main()