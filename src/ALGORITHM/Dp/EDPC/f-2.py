'''
LCS : Longest Common Subsequence
'''
def run(s,t):
    '''
    dp[i+1][j+1] := 文字列 s から i 番目まで、文字列 t から j 番目までの文字をそれぞれ選んだ時の LCS 
    文字列を毎回作ってると tle になっちゃうから、最初に LCS の長さを求めて後はゴリゴリ作っていく
    '''
    s_len, t_len = len(s), len(t)
    # dp = [['']*(t_len+1) for _ in range(s_len+1)]
    dp = [[0]*(t_len+1) for _ in range(s_len+1)]

    for i in range(s_len):
        _s = s[i]
        for j in range(t_len):
            _t = t[j]
            # dp[i+1][j+1] = dp[i][j] + _t if _s == _t else max(dp[i][j], dp[i][j+1], dp[i+1][j], key=lambda e: len(e))
            dp[i+1][j+1] = dp[i][j] + 1 if _s == _t else max(dp[i][j], dp[i][j+1], dp[i+1][j])
    
    l = dp[s_len][t_len]
    ans = []
    while l > 0:
        if s[s_len-1] == t[t_len-1]:
            ans.append(s[s_len-1])
            l -= 1
            s_len -= 1
            t_len -= 1
        elif dp[s_len-1][t_len] == dp[s_len][t_len]:
            s_len -= 1 #s[s_len] があろうとなかろうと lcs の長さが一緒 = s[s_len] は使わない
        elif dp[s_len][t_len-1] == dp[s_len][t_len]:
            t_len -= 1 #t[t_len] があろうとなかろうと lcs の長さが一緒 = t[t_len] は使わない

    print(''.join(reversed(ans)))

if __name__ == '__main__':
    s = input()
    t = input()
    run(s,t)