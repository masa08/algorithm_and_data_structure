from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 全て同じprefixを保持している場合、最小値と最大値を比べるだけでそれが保証できる。
        m, M = min(strs), max(strs)

        for i, letter in enumerate(m):
            if letter != M[i]:
                return m[:i]
        # len(str) = 1の場合、mをそのままreturnする
        return m
