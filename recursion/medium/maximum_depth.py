class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def maximumDepth(root):
    if root is None: return 0
    return 1 + max(maximumDepth(root.left), maximumDepth(root.right))


