from traversals import findmin

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