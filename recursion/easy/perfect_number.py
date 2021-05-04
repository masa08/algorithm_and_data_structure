def perfectNumberList(n):
    result = ''
    for i in range(2, n+1):
        if i == divisor(i):
            if result == '':
                result += '{}'.format(i)
            else:
                result += '-{}'.format(i)
    if result == '':
        return 'none'
    return result


def divisor(number):
    def _divisorHelper(n):
        result = 1
        for i in range(2, n):
            if n % i == 0:
                result += i
        return result

    return _divisorHelper(number)
