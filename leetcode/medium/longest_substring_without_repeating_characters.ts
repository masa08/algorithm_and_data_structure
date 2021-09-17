function lengthOfLongestSubstring(s: string): number {
  let seen = new Set();
  let left = 0;
  let res = 0;

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left += 1;
    }

    seen.add(s[right]);
    res = Math.max(res, right - left + 1);
  }
  return res;
}
