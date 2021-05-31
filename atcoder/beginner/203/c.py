N, K = map(int, input().split())
AB = []

# N人分繰り返してAB配列にデータを格納
for i in range(N):
    x, y = map(int, input().split())
    AB.append((x, y))

# 順不同なので到達村順にソートする
AB.sort()

for i in range(N):
    # 最初の所持金でフレンドがお金をくれる村に到達できる場合、所持金を加算する
    if (K >= AB[i][0]):
        K += AB[i][1]

# 所持金の分村に進むことができる
print(K)
