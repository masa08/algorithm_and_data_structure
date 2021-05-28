import string


def isPangram(s):
    alphabet = set(string.ascii_lowercase)
    for a in alphabet:
        if a not in s.lower():
            return False

    return True
