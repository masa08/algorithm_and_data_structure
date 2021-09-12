function search(nums: number[], target: number): number {
  let left: number = 0;
  let right: number = nums.length - 1;

  while (left <= right) {
    let pivot: number = left + right; //2
    if (nums[pivot] === target) {
      return pivot;
    } else if (nums[pivot] < target) {
      left = pivot + 1;
    } else {
      right = pivot - 1;
    }
  }

  return -1;
}
