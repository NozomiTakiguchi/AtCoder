import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n+1)] # 隣接リスト

_a = []
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    _a.append(a)
    g[a].append(b)

if len(_a) == 0:
    print(n)
    exit()

from collections import deque

def bfs(u):
    cnt = 0
    queue = deque([u])
    d = [None] * (n+1) # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        cnt += 1
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return cnt

# 0からの各頂点の距離
ans = 0
for i in _a:
    ans += bfs(i)
print(ans)
