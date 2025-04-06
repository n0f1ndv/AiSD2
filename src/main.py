from menu import menu
from bst import *

def main():
    # TODO: get array from command line
    # python src/main.py --tree AVL or BST <<<< array of numbers

    type = 'BST' # BST or AVL get it from command line
    menu([2, 5, 10, 12, 13, 6, 9], type)

if __name__ == "__main__":
    main()