def isPalindromeInteger(n):
    if n < 10:
        return True
    string = str(n)
    for i in range(len(string)):
        if string[i] == string[-i-1]:
            continue
        else:
            return False
    return True
