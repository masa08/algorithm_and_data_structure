def main():
    N = int(input())
    lis = [list(map(int, input().split())) for _ in range(N)]
    option_num = 3
    DP = [[0] * option_num for _ in range(N)]
    DP[0] = lis[0]
    for i in range(1, N):
        # 各要素に対して、前と同一の要素以外との足し合わせで最大値を取る。
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                DP[i][j] = max(DP[i-1][k] + lis[i][j], DP[i][j])

    return max(DP[N-1])


print(main())
