def divisor(number):
    def _divisorHelper(n):
        result = '1'
        for i in range(2, n+1):
            print(i)
            if n % i == 0:
                result += '-{}'.format(i)
        return result

    return _divisorHelper(number)
