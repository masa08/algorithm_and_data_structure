# TODO: 理解中
def main():
    # 入力値格納
    N, W = map(int, input().split())
    w = []
    v = []
    for _ in range(N):
        wt, vt = map(int, input().split())
        w.append(wt)
        v.append(vt)

    # dpテーブル定義
    dp = [[0]*(W + 1) for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j < w[i]:  # 選ばない時
                dp[i+1][j] = dp[i][j]
            else:  # 選ぶ時
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
    return dp[N][W]


print(main())
