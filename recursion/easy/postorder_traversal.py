class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def postorderTraversal(root):
    def _postorderTraversal(root, arr):
        if root is not None:
            _postorderTraversal(root.left, arr)
            _postorderTraversal(root.right,arr)
            arr.append(root.data)

    arr = []
    _postorderTraversal(root, arr)
    return arr


