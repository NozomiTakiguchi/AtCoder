from collections import defaultdict
def run(n,m,x,cy):
    # dp[i+1][j+1]: i 回目までのコイントスで、連続ボーナス j をもらう場合の最大値

    d = defaultdict(int)
    for e in cy:
        d[e[0]] = e[1]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            bonus = d[j+1] if j <= i else 0 # defaultdict(int) なので無かったら 0 が返ってくる
            dp[i+1][j+1] = dp[i][j] + x[i] + bonus

            # i 回目で j = 0 になるのは、その時にコインが裏になったとき
            # コインが裏になったとき、得られるコインは 0 かつカウントをゼロに戻す
            # → i-1 回目の総額を引き継ぐ
            dp[i+1][0] = max(dp[i+1][0], dp[i][j]) 

    ans = 0
    for e in dp[n]:
        ans = max(ans, e)
    
    print(ans)


if __name__ == '__main__':
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    cy = [list(map(int, input().split())) for _ in range(m)]
    run(n,m,x,cy)