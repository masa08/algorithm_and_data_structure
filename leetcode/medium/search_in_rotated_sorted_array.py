# TODO: 以下の解法を理解する
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max_num = max(nums)
        index = nums.index(max_num)
        first_arr = nums[0:index+1]
        second_arr = nums[index+1:len(nums)]

        first_search = self.binarySearch(first_arr, target)
        second_search = self.binarySearch(second_arr, target)

        if second_search != -1:
            return second_search + len(first_arr)

        return first_search

    def binarySearch(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right -= 1
            else:
                left += 1
        return -1
