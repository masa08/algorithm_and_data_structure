function containsDuplicate(nums: number[]): boolean {
  let seen = new Map<number, number>();

  for (const num of nums) {
    if (num in seen) {
      return true;
    }
    seen[num] = 0;
  }

  return false;
}
