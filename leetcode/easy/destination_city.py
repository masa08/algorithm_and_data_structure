from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pairs = {}

        for path in paths:
            pairs[path[0]] = path[1]

        for src, dest in paths:
            if dest not in pairs:
                return dest
