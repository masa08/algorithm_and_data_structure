from typing import List


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_rec(numbers: List[int], value: int) -> int:
    def _binary_search_rec(numbers: List[int], value: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search_rec(numbers, value, mid + 1, right)
        else:
            return _binary_search_rec(numbers, value, left, mid - 1)

    return _binary_search_rec(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 14]
    print(binary_search(nums, 15))
    print(binary_search_rec(nums, 15))
