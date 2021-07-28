class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstSearch(root,key):
    if root is None: return None
    if root.data == key: return root
    left = bstSearch(root.left, key)
    right = bstSearch(root.right, key)

    return right if right else left
