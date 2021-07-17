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

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def _postorderTraversal(self, root: TreeNode) -> List[int]:
            # basecase
            if root is None:
                return

            # postorder => rootを最後に評価
            # https://engineer.yeele.net/algorithm/data-structure/binary-tree-traversal/
            _postorderTraversal(self, root.left)
            _postorderTraversal(self, root.right)
            self.ans.append(root.val)

        _postorderTraversal(self, root)
        return self.ans
