# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def diff(self, node):
            if node is None:
                return
            diff(self, node.left)
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            diff(self, node.right)

        self.ans = float('inf')
        self.prev = float('-inf')
        diff(self, root)
        return self.ans
