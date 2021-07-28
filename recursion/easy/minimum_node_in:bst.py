class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def minimumNode(root):
    if root.left is None:
        return root
    result = minimumNode(root.left)
    return result
