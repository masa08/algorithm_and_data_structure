function reverseWords(s: string): string {
  let res = "";
  let word = "";

  for (let c of s) {
    if (c == " ") {
      res += word + c;
      word = "";
    } else {
      word = c + word;
    }
  }

  return res + word;
}
