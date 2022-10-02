# dp でフラグ保持しといて、最後に復元する
def run(n,s):
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))

    # dp[i+1][j+1] : i 枚目までのカードを使って j を作ることができるかどうか
    dp = [[False]*(s+1) for _ in range(n+1)]
    dp[0][0] = True

    for i in range(n):
        a,b = l[i]
        for j in range(s):
            if j+1-a < 0 and j+1-b < 0:
                continue
            
            # i 枚目までの全てのカードを使う問題だから、ひとつ前の値の据え置き、という選択肢は無い。
            # i-1 枚目までの全てのカードを使って j-a or j-b になっていれば dp[i+1][j+1] = True
            if j+1-a >= 0 and dp[i][j+1-a]:
                dp[i+1][j+1] = True
            if j+1-b >= 0 and dp[i][j+1-b]:
                dp[i+1][j+1] = True
    
    if not dp[n][s]:
        print('No')
        exit()
    else:
        print('Yes')

    ans = []
    for i in range(n)[::-1]:
        a,b = l[i]
        # 合計が S になる組み合わせの一例を出せばよい。Yes の場合、i-1 枚目で s-a or s-b が True であることは確定なので、 for を回し終わったタイミングで s = 0 になる (s が 0 がどうかの判定は不要)
        if dp[i][s-a]:
            ans.append('H')
            s-=a
        elif dp[i][s-b]:
            ans.append('T')
            s-=b
    
    ans = reversed(ans)
    print(''.join(ans))


if __name__ == '__main__':
    n,s = map(int, input().split())
    run(n,s)