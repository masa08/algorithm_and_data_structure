def main():
    N = input()
    nuts = list(map(int, input().split()))
    count = 0

    for i in range(int(N)):
        if nuts[i] <= 10:
            continue
        else:
            count = count + (nuts[i] - 10)
    return count


print(main())
