# https://qiita.com/keisuke-ota/items/7190e84019a8c70a9fa6

'''
EDPC G が動的計画法×トポロジカルソートなので、それをやってみる
'''
from collections import defaultdict

def run(n,m,xy):
    print(n,m,xy)

    d = defaultdict(list)
    for e in xy:
        d[e[0]].append(e[1])
    
    l = [[] for _ in range(n)]
    for k,v in d.items():
        l[k-1] = v
    
    print(l)



if __name__ == '__main__':
    n,m = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(m)]
    run(n,m,xy)

