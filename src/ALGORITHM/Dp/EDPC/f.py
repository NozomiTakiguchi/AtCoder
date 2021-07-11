_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    s = _i()
    t = _i()

    # # 長さが短い文字列を s にする
    # if len(s) > len(t):
    #     s,t = t,s
    
    # N = len(s)
    # dp = [''] * (N + 1) # dp[i] = i-1 番目までを選択して作成可能な部分文字列 

    # for i in range(N):
    #     _s = dp[i] + s[i]
    #     # 順序を維持したまま、他方の文字列に _s が含まれるかどうかを検証するのが難しい (dp[i] + s[i] not in t だと、部分列の評価ができない)
    #     dp[i+1] = dp[i] if dp[i] + s[i] not in t else [dp[i] + s[i], dp[i]][len(dp[i]+s[i]) > len(dp[i])]
    
    # print(dp[N])


    # 1 linear で書く時のインデックス注意する！
    dp = [[0]*(len(t)+1) for _ in range(len(s)+1)] # dp[i][j] : s を i-1 番目、 t を j-1 番目まで調べた時の部分列の文字長の最大値

    slen = len(s)
    tlen = len(t)

    # 先に長さだけ求める
    for i in range(slen):
        for j in range(tlen):
            dp[i+1][j+1] = dp[i][j] + 1 if s[i] == t[j] else max(dp[i+1][j], dp[i][j+1])
    
    ans = ''
    while slen > 0 and tlen > 0:
        if dp[slen][tlen] == dp[slen-1][tlen]:
            slen -= 1
        elif dp[slen][tlen] == dp[slen][tlen-1]:
            tlen -= 1
        else:
            ans += s[slen-1]
            slen -= 1
            tlen -= 1
    
    print(ans[::-1])

    

if __name__ == '__main__':
    run()