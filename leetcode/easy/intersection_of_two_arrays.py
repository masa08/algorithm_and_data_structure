from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set_nums1 = list(set(nums1))
        set_nums2 = list(set(nums2))

        for n1 in set_nums1:
            if n1 in set_nums2:
                result.append(n1)

        return result

