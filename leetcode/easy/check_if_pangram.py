import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        for a in alphabet:
            if a not in sentence.lower():
                return False

        return True
