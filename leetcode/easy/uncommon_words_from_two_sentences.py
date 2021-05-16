from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mapping = {}
        for s in s1.split(" ") + s2.split(" "):
            if s in mapping:
                mapping[s] += 1
            else:
                mapping[s] = 1

        result = []
        for k, v in mapping.items():
            if v == 1:
                result.append(k)

        return result
