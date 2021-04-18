from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        even.extend(odd)

        return even
