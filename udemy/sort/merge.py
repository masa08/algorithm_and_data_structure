from typing import List

def merge_sort(numbers: List[int]) -> List[int]:
  if len(numbers) <= 1: return numbers

  center = len(numbers) // 2
  left = numbers[:center]
  right = numbers[center:]

  merge_sort(left)
  merge_sort(right)

  i = j = k = 0

  # k = i + jとなる
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      numbers[k] = left[i]
      i += 1
    else:
      numbers[k] = right[j]
      j += 1
    k += 1

  # 考慮されなかった余った部分に対する処理
  while i < len(left):
    numbers[k] = left[i]
    i += 1
    k += 1

  while j < len(right):
    numbers[k] = right[j]
    j += 1
    k += 1

  return numbers


if __name__ == '__main__':
  nums = [1, 8, 3, 9, 4, 5, 7]
  print(merge_sort(nums))
