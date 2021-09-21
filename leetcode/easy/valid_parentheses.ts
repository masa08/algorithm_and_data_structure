function isValid(s: string): boolean {
  const stack = [];
  const map = { ")": "(", "}": "{", "]": "[" };

  for (let c of s) {
    if (c in map) {
      let topElement = stack ? stack.pop() : "#";
      if (map[c] != topElement) return false;
    } else {
      stack.push(c);
    }
  }

  return stack.length === 0;
}
