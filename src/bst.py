class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


# INSERTING ELEMENTS INTO BST
def insert(root, key):
    tmp = Node(key)

    if root is None:
        return tmp
    
    parent = None
    current = root
    while current is not None:
        parent = current
        #print(f'key ... current.key: {key} ... {current.key}')
        if key < current.key:
            current = current.left
        elif key > current.key:
            current = current.right
        else:
            return root # key already exists
        
    if key < parent.key:
        parent.left = tmp
        #print(f'par {parent.key}')
    else:
        parent.right = tmp
        #print(f'par {parent.key}')

    return root


def create_tree(lst):
    print(f'Inserting...', end=' ')
    for num in lst:
        print(f'{num}', end=' ')
    print()

    root = Node(lst[0])
    for num in lst[1:]:
        root = insert(root, num)

    return root


# TRAVERSING BST
def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)


def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')


# FINDING MIN MAX IN BST
def findmin(node):
    while node.left is not None:
        node = node.left

    return node
    

def findmax(node):
    while node.right is not None:
        node = node.right

    return node


# DELETING FROM BST
def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = findmin(root.right)
        root.key = temp.key

        root.right = delete(root.right, temp.key)

    return root


def delete_all(root):
    if root:
        delete_all(root.left)
        delete_all(root.right)
        root = None

    return root


# BALANCING BST
def sort_inorder(root, nodes):
    if root:
        sort_inorder(root.left, nodes)
        nodes.append(root.key)
        sort_inorder(root.right, nodes)

    return nodes


def build_balanced_tree(nodes, start, end):
    if start > end:
        return

    middle = (start + end) // 2
    root = Node(nodes[middle])

    root.left = build_balanced_tree(nodes, start, middle - 1)
    root.right = build_balanced_tree(nodes, middle + 1, end)

    return root