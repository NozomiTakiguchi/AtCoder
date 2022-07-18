'''
品物 i : 価値 vi / 重さ wi
ナップサック : W
dp[i][l] : 品物 i までを選択したとき、重さ j までの価値の総和の最大 → これ思いつくのむずくね？？？
持ち帰る荷物の総重量は W 以下 → 総重量 W となる時の価値の総和を求める、として dp[i][j] お置くのがよさそう.
dp[i-1][j-xx] のほうが i 番目を持って帰るよりも価値の総和が高い場合があるが、その場合はひとつ前の価値の総和を引き継げばよいので、求めたい値は dp[i][j] でよい

'''
def run(n,w,wv):
    dp = [[0]*w for _ in range(n)]

    for i in range(n):
        weight,value = wv[i]

        for j in range(w):
            if i == 0:
                # index で重さを管理してるから weight-1 番目 が weight までの価値の総和
                dp[i][j] = 0 if weight-1 > j else value # ナップサックの重量を超える場合は暗黙的に対象外になる
            else:
                # i 番目の荷物が重さ weight なので、i 番目をナップサックに入れるときは表的には i-1 番目の重さが j-weight の時に i 番目の荷物を入れることができる
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value) if j-weight >= 0 else dp[i-1][j]
    
    print(dp[n-1][w-1])

if __name__ == '__main__':

    n,w = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    run(n,w,wv)