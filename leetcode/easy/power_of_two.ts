function isPowerOfTwo(n: number): boolean {
  while (n > 1) {
    n /= 2;
  }
  if (n === 1) return true;
  return false;
}
