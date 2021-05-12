# https://www.youtube.com/watch?v=r3xN36so6Jg
# https://engineer.yeele.net/algorithm/leetcode-easy-589-n-ary-tree-preorder-traversal/
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        def _preorder(root):
            if root is None:
                return
            result.append(root.val)
            for child in root.children:
                _preorder(child)

        result = []
        _preorder(root)
        return result
