from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            # 個数に関しては対応できるが隣接まで対応できない
            if s2[i] in counter:
                counter[s2[i]] -= 1
            # i-w is checking of the begning letter inside the current sliding window
            # sliding window内にs1文字列が全て含まれている必要がある
            # この条件に該当するということは、swの中に対象文字列が存在しない
            # つまり、連続した文字列ではないということになる。
            if i >= w and s2[i-w] in counter:
                counter[s2[i-w]] += 1

            if all([counter[i] == 0 for i in counter]):
                return True

        return False
