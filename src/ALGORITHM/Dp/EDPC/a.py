ni = lambda: int(_n())
nl = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    # インデックスは i = k-1 (k : 1 <= k <= n)
    # dp[] は n+1 の長さ (dp[0]: 初期値 / dp[k+1]: k 番目までの要素 (インデックスは i = k-1) にかかる何らかの結果)

    n = ni()
    h = nl()

    dp = [0] * (n+1) # dp[k+1] : 足場 k (インデックスは i = k-1) に到着するまでの最小到達コストを格納したい
    for i in range(1,n):
        if i-2 < 0:
            dp[i+1] = dp[i] + abs(h[i] - h[i-1])
        else:
            # 足場 i-1 までの最小到達コスト + 足場 i までのコスト と
            # 足場 i-2 までの最小到達コスト + 足場 i までのコスト を比較する
            dp[i+1] = min(dp[i] + abs(h[i] - h[i-1]), dp[i-1] + abs(h[i] - h[i-2]))
    
    print(dp[n])

if __name__ == '__main__':
    run()
