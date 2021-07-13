# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrder(self, arr, li):
        if not arr:
            li.append(None)
        else:
            li.append(arr.val)
            self.preOrder(arr.left, li)
            self.preOrder(arr.right, li)
        return li

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pl = self.preOrder(p, [])
        ql = self.preOrder(q, [])
        return(pl == ql)
