function firstUniqChar(s: string): number {
  let map = new Map();

  for (let v of s) {
    if (v in map) {
      map[v] += 1;
    } else {
      map[v] = 1;
    }
  }

  let index = -1;
  for (let i = 0; i < s.length; i++) {
    if (map[s[i]] == 1) {
      index = i;
      break;
    }
  }

  return index;
}
