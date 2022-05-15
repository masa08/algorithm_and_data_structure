# https://dev.classmethod.jp/articles/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/742926/Simple-Explanation-or-Concise-or-Thinking-Process-and-Example
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = {}
        left, right = 0, 0
        longest = 1
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]]+1)
            longest = max(longest, right - left + 1)
            seen[s[right]] = right
            right += 1
        return longest


class SolutionTwo:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, res = 0, 0

        for i in range(len(s)):
            # iがseenから無くなるまで、remove
            while s[i] in seen:
                seen.remove(s[l])
                # removeした分、lを進める
                l += 1
            seen.add(s[i])
            res = max(res, i-l+1)
        return res
