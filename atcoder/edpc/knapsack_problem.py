# input example
# 3 8
# 3 30
# 4 50
# 5 60
# https://www.mrrhp.com/ja/understandable-knapsack#_4
# https://nashidos.hatenablog.com/entry/2020/05/09/071907
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

    # Nとweightとvalueは同じ長さで連動している
    # N = 3, W = 8
    # weight = [3, 4, 5]
    # value = [30, 50, 60]
    for i in range(N):
        for j in range(W+1):
            # jが該当itemの重さを超えたタイミングで選択が発生
            if j >= w[i]: # 選択ロジック
                # 一つ前段階の合計の重さと
                # それに自身の重さを加算した場合の比較
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
            else: # 選択しない
                dp[i+1][j] = dp[i][j]

    return dp[N][W]


print(main())
