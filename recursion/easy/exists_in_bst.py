class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def exists(root,key):
    if root is None: return False
    if root.data == key: return True
    left = exists(root.left, key)
    right = exists(root.right, key)

    return left or right
