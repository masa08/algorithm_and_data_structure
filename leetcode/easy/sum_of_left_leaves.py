# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0

        def _sumOfLeftLeaves(root):
            if not root.left and not root.right:
                return
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.total += root.left.val
                _sumOfLeftLeaves(root.left)
            if root.right:
                _sumOfLeftLeaves(root.right)

        _sumOfLeftLeaves(root)
        return self.total

    def sumOfLeftLeavesRefactor(self, root: TreeNode) -> int:
        self.total = 0
        def _sumOfLeftLeaves(root):
            if not root:
                return
            if root.left and root.left.left is None and root.left.right is None:
                self.total += root.left.val
            _sumOfLeftLeaves(root.left)
            _sumOfLeftLeaves(root.right)

        _sumOfLeftLeaves(root)
        return self.total
