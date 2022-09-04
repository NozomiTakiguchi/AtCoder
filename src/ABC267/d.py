'''
始めてコンテスト問題で (ほぼ) 自力で dp の問題解けた ... !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
def run(n,m,a):
    INF = -float('inf')
    dp = [[INF]*(m+1) for _ in range(n+1)]
    # dp[i+1][j+1] : i 番目時点で j　個要素を選んだ時の合計値の最大

    dp[1][1] = a[0]
    for i in range(n):
        for j in range(m):
            _a = a[i]

            if j == 0:
                dp[i+1][j+1] = max(dp[i][j+1], _a)
                continue
            if j == i:
                dp[i+1][j+1] = dp[i][j]+(j+1)*_a # それまでの要素を1つずつ選ぶしかない
                continue
            # i > j のとき
            # i 番目までに j 個選ぶときの選択肢 → i-1 番目までに j 個選んだ時と、 i 番目の値を用いた時の合計値の大きいほう
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (j+1)*_a)
    print(dp[n][m])

if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))

    run(n,m,a)