import sys
from menu import menu

# TODO: I need to check if dependencies are imported correctly

# def main():
#     # TODO: get array from command line
#     # python src/main.py --tree AVL or BST <<<< array of numbers
#     # if users will give the wrong tree type close the program

#     # BST or AVL get it from command line
#     # def menu(lst, type)
#     menu([2, 5, 10, 12, 13, 6, 9], input('tree type> ').upper())

# if __name__ == "__main__":
#     main()


def main():
    #python src/main.py --tree AVL or BST <<<< array of numbers
    if len(sys.argv) != 3 or sys.argv[1] != "--tree":
        print("Usage: python src/main.py --tree AVL or BST <<<< array of numbers")
        sys.exit(1)
    
    tree_type = str(sys.argv[2])
    if tree_type != "AVL" and tree_type != "BST":
        print("Error: Invalid tree type. Use 'AVL' or 'BST'.")
        sys.exit(1)

    input=sys.stdin.readline().split()
    try:
        data=[int(x) for x in input]
    except EOFError:
        print("Error reading input.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
        sys.exit(1)

    if len(data) == 0 or not data:
        print("Error: No input provided")
        sys.exit(1)
    
    menu(data, tree_type)



if __name__ == "__main__":
    main()