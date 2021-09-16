# pivotより小さい数、大きい数を整理して、再帰的に繰り返すことによりソートを実行する。
from typing import List


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    # i+1以下はnumbers[high]よりも小さく、i+1以上はnumbers[high]より大きい
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            # pivotの左側
            _quick_sort(numbers, low, partition_index - 1)
            # pivotの右側
            _quick_sort(numbers, partition_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))
