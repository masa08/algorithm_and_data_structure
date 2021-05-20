class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for a in address:
            if a == ".":
                result += "[.]"
                continue
            result += a
        return result
