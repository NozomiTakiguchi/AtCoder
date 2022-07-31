def run(n,m,uv):
    # 頂点 i,j を結ぶ辺がある場合 True
    adj = [[False]*n for _ in range(n)]

    for e in uv:
        adj[e[0]-1][e[1]-1] = True
        adj[e[1]-1][e[0]-1] = True
    
    ans = 0

    for i in range(n):
        for j in range(i+1, n): # +1 するの、調べる箇所の重複を避けるため、ってのは分かるけど自分では思いつかないな、、
            for k in range(j+1, n):
                if adj[i][j] and adj[j][k] and adj[k][i]:
                    ans += 1
    
    print(ans)


if __name__ == '__main__':
    n,m = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(m)]
    run(n,m,uv)