import sys
sys.setrecursionlimit(10000)


def dfs(v, tmp, G):
    if tmp[v]:
        return
    tmp[v] = True
    for _v in G[v]:
        dfs(_v, tmp, G)
    
def run(n,m,G):
    ans = 0
    for i in range(n):
        tmp = [False]*n
        dfs(i, tmp, G)
        ans+=sum(tmp)
    
    print(ans)


if __name__ == '__main__':
    n,m = map(int, input().split())
    G = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int, input().split())
        G[a-1].append(b-1)

    run(n,m,G)