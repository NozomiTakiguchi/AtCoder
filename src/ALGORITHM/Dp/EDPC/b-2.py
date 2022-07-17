'''
足場 i から i+1,i+2,...,i+k のどれかへジャンプ. 
'''
def run(n,k,h):
    dp = [0]*n

    for i in range(1,n): # 現在の位置
        
        t = k if i-k > 0 else i # さかのぼれる最大
        dp[i] = min([dp[i-j-1] + abs(h[i]-h[i-j-1]) for j in range(t)])
        # ↑ j-1 にするのにしばらく気づけなかった、、、
        # range(t) -> 0,...,t-1 なので、本当にさかのぼりたいのは j+1
    print(dp[n-1])



if __name__ == '__main__':
    n,k = map(int, input().split())
    h = list(map(int, input().split()))

    run(n,k,h)