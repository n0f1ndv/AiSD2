from menu import menu
import select
import sys

def main():
    stdin_state = select.select([sys.stdin], [], [], 0.0)[0]
    
    if sys.argv[1] != '--tree' or (len(sys.argv)==3 and not stdin_state):
        print('Usage: python src/main.py --tree AVL or BST <<< array of numbers')
        sys.exit(1)
    tree_type = str(sys.argv[2])
    if tree_type != 'AVL' and tree_type != 'BST':
        print('Error: Invalid tree type. Use AVL or BST.')
        sys.exit(1)
    try:
        if len(sys.argv) == 4 and not stdin_state:
            data = [int(x) for x in sys.argv[3].replace(' ',',').split(',')]

        elif len(sys.argv) == 3:
            data=sys.stdin.read()
            data = data.strip().replace(',',' ').replace('\n', ' ')
            data=[int(x.strip()) for x in data.split()]
        else:
            data=[]
            if stdin_state:
                temp = sys.stdin.read().strip().strip(",").split(',')
                for x in temp:
                    data.append(int(x))
            for i in range(3,len(sys.argv)):
                temp=sys.argv[i].strip(',').split(',')
                for x in temp:
                    data.append(int(x))
    
    except EOFError:
        print('Error reading input.')
        sys.exit(1)
    except ValueError:
        print('Error: Invalid integer')
        sys.exit(1)


    if len(data) == 0 or not data:
        print('Error: No input provided')
        sys.exit(1)
    
    tmp = data
    data=[]
    for x in tmp:
        if x not in data:
            data.append(x)
    
    menu(data, tree_type)


if __name__ == '__main__':
    main()