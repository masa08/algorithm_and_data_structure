# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val

        def _isUnivalTree(self, root: TreeNode) -> bool:
            if root is None:
                return True
            if root.val != value:
                return False
            left = _isUnivalTree(self, root.left)
            right = _isUnivalTree(self, root.right)
            return left and right

        return _isUnivalTree(self, root)
