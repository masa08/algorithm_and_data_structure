// 計算量: O(N*logN)
const partition = (numbers: number[], low: number, high: number): number => {
  let i = low - 1;
  const pivot = numbers[high];
  for (let j = low; j < high; j++) {
    if (numbers[j] <= pivot) {
      i += 1;
      const temp = numbers[j];
      numbers[j] = numbers[i];
      numbers[i] = temp;
    }
  }
  const temp = numbers[i + 1];
  numbers[i + 1] = numbers[high];
  numbers[high] = temp;
  return i + 1;
};

const quickSort = (numbers: number[]): number[] => {
  const _quickSort = (numbers: number[], low: number, high: number): void => {
    if (low < high) {
      const partitionIndex = partition(numbers, low, high);
      _quickSort(numbers, low, partitionIndex - 1);
      _quickSort(numbers, partitionIndex + 1, high);
    }
  };
  _quickSort(numbers, 0, numbers.length - 1);
  return numbers;
};

const nums = [1, 8, 3, 4, 5, 7];
console.log(quickSort(nums));
