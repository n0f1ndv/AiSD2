import sys
from menu import menu
import select
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
    if sys.argv[1] != "--tree":
        print("Usage: python src/main.py --tree AVL or BST <<<< array of numbers")
        sys.exit(1)
    
    tree_type = str(sys.argv[2])
    if tree_type != "AVL" and tree_type != "BST":
        print("Error: Invalid tree type. Use 'AVL' or 'BST'.")
        sys.exit(1)
    try:
        if len(sys.argv) == 4:
            data = [int(x) for x in sys.argv[3].replace(' ',",").split(',')]

        elif len(sys.argv) == 3:
            data=sys.stdin.read()
            data = data.strip().replace(' ',",").replace("\n", ",")
            data=[int(x) for x in data.split(",")]
        else:
            data=[]
            if select.select([sys.stdin], [], [], 0.0)[0]:
                temp = sys.stdin.read().strip().split(",")
                for x in temp:
                    data.append(int(x))
            for i in range(3,len(sys.argv)):
                temp=sys.argv[i].strip(",").split(",")
                for x in temp:
                    data.append(int(x))
    
    except EOFError:
        print("Error reading input.")
        sys.exit(1)
    # except ValueError:
    #     print("Error: Invalid integer")
    #     sys.exit(1)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
        sys.exit(1)
    tmp = data
    data=[]
    data = [x for x in tmp if x not in data]
    print(data)
    if len(data) == 0 or not data:
        print("Error: No input provided")
        sys.exit(1)
    menu(data, tree_type)



if __name__ == "__main__":
    main()


# TODO: I need to check if dependencies are imported correctly

# def main():
#     #python src/main.py --tree AVL or BST <<<< array of numbers
    
#     tree_type = str(sys.argv[2])
    
#     if len(sys.argv) == 4:
#         print(sys.argv[3].split(","))
#         data = [int(x) for x in sys.argv[3].split(',')]
#     elif len(sys.argv) > 4:
#         print("Error: Wrong input")
#         sys.exit(1)
#     else:
#         data=[int(x) for x in sys.stdin.readline().split()]

#     menu(data, tree_type)


# if __name__ == '__main__':
#     main()
        # else:
        #     data=[]
        #     temp=sys.stdin.read().split(",")
        #     for i in temp:
        #         for x in i.split():
        #             data.append(int(x))