function sortedSquares(nums: number[]): number[] {
  let result: number[] = [];
  let left: number = 0;
  let right: number = nums.length - 1;

  for (var i = nums.length - 1; i >= 0; i--) {
    if (Math.abs(nums[left]) >= Math.abs(nums[right])) {
      result.unshift(nums[left] ** 2);
      left += 1;
    } else {
      result.unshift(nums[right] ** 2);
      right -= 1;
    }
  }
  return result;
}
