# TODO: 理解する
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        i = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j += 1
        return i == len(name)
