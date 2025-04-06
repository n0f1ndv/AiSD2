from menu import menu

# TODO: I need to check if dependencies are imported correctly

def main():
    # TODO: get array from command line
    # python src/main.py --tree AVL or BST <<<< array of numbers
    # if users will give the wrong tree type close the program

    # BST or AVL get it from command line
    # def menu(lst, type)
    menu([2, 5, 10, 12, 13, 6, 9], input('tree type> '))

if __name__ == "__main__":
    main()