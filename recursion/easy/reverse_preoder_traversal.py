class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def reverseInorderTraversal(root):
    def _reverseInorderTraversal(root, arr):
        if root is not None:
            _reverseInorderTraversal(root.right,arr)
            arr.append(root.data)
            _reverseInorderTraversal(root.left, arr)

    arr = []
    _reverseInorderTraversal(root, arr)
    return arr



