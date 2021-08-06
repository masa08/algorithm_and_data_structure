class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def inorderTraversal(root):
    #ここから書きましょう
    def _inorderTraversal(root, arr):
        if root is not None:
            _inorderTraversal(root.left, arr)
            arr.append(root.data)
            _inorderTraversal(root.right,arr)

    arr = []
    _inorderTraversal(root, arr)
    return arr

