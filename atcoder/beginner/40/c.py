def main():
    N = int(input())
    h = list(map(int, input().split()))

    DP = [0]*N
    DP[1] = abs(h[1]-h[0])
    for i in range(2, N):
        DP[i] = min(abs(h[i]-h[i-2])+DP[i-2], abs(h[i]-h[i-1])+DP[i-1])
    return DP[-1]


print(main())
