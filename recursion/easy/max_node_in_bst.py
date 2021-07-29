class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def maximumNode(root):
    if root.right is None:
        return root
    return maximumNode(root.right)
