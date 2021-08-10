class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def symmetricTree(root):
    if root is None: return True
    left = inorderTraversal(root.left)
    right = reverseInorderTraversal(root.right)

    return left == right

def inorderTraversal(root):
    def _inorderTraversal(root, arr):
        if root is None:
            arr.append(None)
            return
        if root.right is None and root.left is None:
            arr.append(root.data)
            return
        _inorderTraversal(root.left, arr)
        arr.append(root.data)
        _inorderTraversal(root.right, arr)
    arr = []
    _inorderTraversal(root, arr)

    return arr

def reverseInorderTraversal(root):
    def _reverseInorderTraversal(root, arr):
        if root is None:
            arr.append(None)
            return
        if root.right is None and root.left is None:
            arr.append(root.data)
            return
        _reverseInorderTraversal(root.right, arr)
        arr.append(root.data)
        _reverseInorderTraversal(root.left, arr)
    arr = []
    _reverseInorderTraversal(root, arr)

    return arr
