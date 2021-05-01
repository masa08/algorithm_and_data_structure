def notDivided(x, y):
    def notDividedHelper(x, y):
        result = '1'
        for i in range(2, x+1):
            if i % y == 0:
                continue
            result += '-{}'.format(i)
        return result

    return notDividedHelper(x, y)
