def run(n,a):
    # dp = [0]*n
    # prev = 100 # 0,1,2 以外で何でもいい
    # '''
    # 1 次元配列だと単純に前日の選択肢を外して最大値を採ることしかできず、全体最適化が出来ない
    # T日 : 100,0,1 / T+1 日: 1000, 1, 0 みたいな時、1 次元配列だと max = 101 になってしまう. 本当は 1001 が答え
    # '''
    # for i in range(n):
    #     if i == 0:
    #         dp[i], prev = max(([elm, cnt] for cnt,elm in enumerate(a[i])), key=lambda n: n[0])
    #     else:
    #         print(prev)
    #         c, prev = max(filter(lambda n: n[1] != prev, ([elm, cnt] for cnt,elm in enumerate(a[i]))))
    #         dp[i] = dp[i-1] + c

    '''
    選択肢 x を採ったときの最大値をそれぞれ計算して、各最大値のさらに最大値を選んでいく
    → 前日の選択肢を除いて毎日幸福度が最大の活動をすると全体の最適化ができない
    → 日毎に、選択肢 x を採ったときの幸福度の累積を計算して、それが最大になるものを毎回選ぶ
    '''
    dp = [[0]*3 for _ in range(n)]
    for i in range(n):
        for j in range(3):
            if i == 0:
                    dp[i][j] = a[i][j]
            else:
                dp[i][j] = max(dp[i-1][k] + a[i][j] for k in range(3) if k != j)

    print(max(dp[n-1]))


if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    run(n,a)