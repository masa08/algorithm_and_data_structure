from typing import List


class Solution:
    def diStringMatch(self, String: str) -> List[int]:
        start, last = 0, len(String)
        result = []
        for char in String:
            if char == "I":
                result.append(start)
                start += 1
            else:
                result.append(last)
                last -= 1
        result.append(start)
        return result
