from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def _inorderTraversal(self, root: TreeNode, res: List[int]) -> None:
            if root:
                _inorderTraversal(self, root.left, res)
                res.append(root.val)
                _inorderTraversal(self, root.right, res)
        res = []
        _inorderTraversal(self, root, res)
        return res
