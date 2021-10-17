// 計算量: O(n**2)
const bubbleSort = (numbers: number[]): number[] => {
  const len = numbers.length;

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len - 1 - i; j++) {
      if (numbers[j] > numbers[j + 1]) {
        let temp = numbers[j];
        numbers[j] = numbers[j + 1];
        numbers[j + 1] = temp;
      }
    }
  }

  return numbers;
};

const numbers = [2, 5, 1, 8, 7, 3];
console.log(bubbleSort(numbers));
