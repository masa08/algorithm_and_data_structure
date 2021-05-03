class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}

        for i in s:
            if i in seenS:
                seenS[i] += 1
            else:
                seenS[i] = 1

        for j in t:
            if j in seenT:
                seenT[j] += 1
            else:
                seenT[j] = 1

        if seenS == seenT:
            return True
        return False
