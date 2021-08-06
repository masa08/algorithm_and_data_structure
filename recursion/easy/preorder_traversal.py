class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorderTraversal(root):
    def _preorderTraversal(root, arr):
        if root is not None:
            arr.append(root.data)
            _preorderTraversal(root.left, arr)
            _preorderTraversal(root.right,arr)

    arr = []
    _preorderTraversal(root, arr)
    return arr
