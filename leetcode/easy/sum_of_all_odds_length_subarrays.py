from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            # range(start, stop, step)で偶数ごとに呼び出し
            for j in range(i, len(arr), 2):
                # +1することで奇数に
                result += sum(arr[i:j+1])

        return result
