# input example
# 4
# 10 30 40 20

def main():
    N = int(input())
    h = list(map(int, input().split()))

    # init list for dp
    DP = list(0 for _ in range(N))

    # fix first and second cost
    DP[0] = 0
    DP[1] = abs(h[1]-h[0])

    for i in range(2, N):
        costFromTwoStepsBefore = DP[i-2] + abs(h[i]-h[i-2]);
        costFromOneStepBefore = DP[i-1] + abs(h[i]-h[i-1]);
        DP[i] = min(costFromTwoStepsBefore, costFromOneStepBefore)

    return DP[-1]


print(main())
