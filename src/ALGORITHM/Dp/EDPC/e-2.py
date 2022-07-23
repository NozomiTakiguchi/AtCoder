'''
ナップサック問題だが、 w が 10^9 まで定義できるため d.py と同じコードで for loop すると MemoryError になる
dp[i][j] = 重さ で考える
i 番目までの荷物をいくつか選んだ時の、価値の総和 j までの総重量の最小 (総重量 w までの価値の総和の最大と同値？？)

→ インデックスが全然わからん。
ちゃんと絵にかいたらイメージできる？
'''
def run(n,w,wv):

    l = 0
    for e in wv:
        l += e[1] # 渡された配列から、取りうる価値の最大値を計算する
    
    INF = float('inf')
    dp = [[INF]*(l+1) for _ in range(n+1)]
    dp[0][0] = 0 # これやらんと答えがうまく出なくなる理由もよくわからない

    for i in range(n):
        weight, value = wv[i]

        for j in range(l+1):
            dp[i+1][j] = dp[i][j] if j - value < 0 else min(dp[i][j], dp[i][j-value]+weight)

    ans = 0
    for idx, e in enumerate(dp[n]):
        if e <= w:
            ans = max(ans, idx)
    
    print(ans)


if __name__ == '__main__':

    n,w = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    run(n,w,wv)