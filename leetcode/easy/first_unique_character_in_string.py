class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for string in s:
            if string not in d:
                d[string] = 1
            else:
                d[string] += 1

        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break

        return index
