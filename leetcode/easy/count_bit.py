from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            two = bin(i)
            count = str(two).count('1')
            result.append(int(count))
        return result
