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


def findmin(node):
    while node.left is not None:
        node = node.left

    return node
    

def findmax(node):
    while node.right is not None:
        node = node.right

    return node