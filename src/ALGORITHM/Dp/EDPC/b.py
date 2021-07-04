ni = lambda: int(_n())
nl = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():

    n,k = nl()
    h = nl()

    dp = [0 for _ in range(n+1)] # dp[k+1] : 足場 k (index: i = k-1) までの最小到達コスト
    for i in range(1,n):
        c = k if i - k > 0 else i # さかのぼれる足場の最大数

        # 基本 index で考える (dp が順番一つずれたり渡されるリストが 1 始まりで分かりづらいため)
        # i 番目dp = i-1 番目 dp + ${i-1 番目から i 番目に異動するコスト}
        #→ dp[i+1] = dp[i] + abs(h[i] (ここは固定) - h[i-1]) を変形させる

        dp[i+1] = min([dp[i-j] + abs(h[i] - h[i-j-1]) for j in range(c)])

    print(dp[n])


if __name__ == '__main__':
    run()