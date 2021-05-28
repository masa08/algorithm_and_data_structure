def primesUpToNCount(n):
    isPrime = [False, False] + [True] * (n-2)
    current = 2
    while current**2 < n:
        if isPrime[current]:
            i = current**2
            while i < n:
                isPrime[i] = False
                i += current
        current += 1

    return sum(isPrime)
