class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = []
        for string in s:
            stack.append(string)

        for target in t:
            if stack and target == stack[0]:
                stack.pop(0)
            else:
                continue

        if not stack:
            return True
        else:
            return False
