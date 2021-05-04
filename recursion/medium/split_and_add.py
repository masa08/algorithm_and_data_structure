import math


def splitAndAdd(digits):
    def _splitAndAdd(digits):
        if digits < 1:
            return 0
        rest = digits % 10
        digits = math.floor(digits / 10)

        return rest + _splitAndAdd(digits)

    return _splitAndAdd(digits)
