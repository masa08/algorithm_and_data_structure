from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def _preorderTraversal(self, root: TreeNode) -> List[int]:
            if root is None:
                return
            self.ans.append(root.val)
            _preorderTraversal(self, root.left)
            _preorderTraversal(self, root.right)

        _preorderTraversal(self, root)
        return self.ans
