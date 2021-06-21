# https://www.mrrhp.com/ja/understandable-knapsack#_4
# https://nashidos.hatenablog.com/entry/2020/05/09/071907
def main():
    # 入力値格納
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        wt, vt = map(int, input().split())
        weight.append(wt)
        value.append(vt)

    # dpテーブル定義
    dp = [[0]*(W + 1) for _ in range(N+1)]

    # Nとweightとvalueは同じ長さで連動している
    # N = 3, W = 8
    # weight = [3, 4, 5]
    # value = [30, 50, 60]
    for i in range(N):
        for w in range(W+1):
            if w < weight[i]:  # 選ばない
                dp[i+1][w] = dp[i][w]
            else:  # 選ぶ
                dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]]+value[i])
        print(dp)

    return dp[N][W]


print(main())
