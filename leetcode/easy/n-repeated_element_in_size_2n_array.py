from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        mapping = []

        for n in A:
            if n in mapping:
                return n
            else:
                mapping.append(n)
