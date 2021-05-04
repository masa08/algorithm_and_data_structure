def reverseString(string):
    def _reverseString(string, result):
        if string == '':
            return result
        result += string[-1]
        string = string[:-1]
        return _reverseString(string, result)

    return _reverseString(string, '')
