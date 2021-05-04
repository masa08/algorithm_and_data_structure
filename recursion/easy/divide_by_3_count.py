def divideBy3Count(n):
    def _divideBy3Count(n, count):
        if n == 1:
            return count
        count += 1
        return _divideBy3Count(n//3, count)

    return _divideBy3Count(n, 0)
