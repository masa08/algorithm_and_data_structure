function maxSubArray(nums: number[]): number {
  let numsLen: number = nums.length;
  let cur_sum: number = nums[0];
  let max_sum: number = nums[0];

  for (let i = 1; i < numsLen; i++) {
    cur_sum = Math.max(nums[i], cur_sum + nums[i]);
    max_sum = Math.max(max_sum, cur_sum);
  }

  return max_sum;
}
