from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1[:] = sorted(nums1[:m] + nums2[:n])
        nums1[:] = nums1[:m] + nums2[:n]
        self.bubble_sort(nums1)

    def bubble_sort(self, numbers: List[int]) -> List[int]:
        len_numbers = len(numbers)

        for i in range(len_numbers):
            for j in range(len_numbers - 1 - i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers
