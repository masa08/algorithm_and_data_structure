from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, N+1):
            # trustedのvalueが人数分を満たしていたら
            if trusted[i] == N-1:
                return i
        return -1
