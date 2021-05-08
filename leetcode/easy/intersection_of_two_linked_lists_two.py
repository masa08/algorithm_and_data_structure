# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums2:
            if n in nums1:
                result.append(n)
                nums1.remove(n)

        return result

# two pointer
# class Solution(object):
#     def intersect(self, nums1, nums2):

#         nums1, nums2 = sorted(nums1), sorted(nums2)
#         pt1 = pt2 = 0
#         res = []

#         while True:
#             try:
#                 if nums1[pt1] > nums2[pt2]:
#                     pt2 += 1
#                 elif nums1[pt1] < nums2[pt2]:
#                     pt1 += 1
#                 else:
#                     res.append(nums1[pt1])
#                     pt1 += 1
#                     pt2 += 1
#             except IndexError:
#                 break

#         return res
