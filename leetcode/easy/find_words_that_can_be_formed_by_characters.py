from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        for w in words:
            d = {}
            for c in chars:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

            count = 0
            for l in w:
                if l in d and d[l] > 0:
                    d[l] -= 1
                    count += 1
                else:
                    count = 0
                    break
            result += count
        return result
