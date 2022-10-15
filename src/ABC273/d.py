'''
二分探索でいけるらしい
'''
from collections import defaultdict
vect = {
    'L':-1,
    'R':1,
    'U':1,
    'D':-1
}

def run():
    H,W,rs,cs = map(int, input().split())
    n = int(input())

    dic = defaultdict(list)
    ddic = defaultdict(list)
    for _ in range(n):
        r,c = map(int, input().split())
        dic[r].append(c)
        ddic[c].append(r)

    q = int(input())
    for _ in range(q):
        d, l = input().split()
        l = int(l)
        cnt = l*vect[d]
        wall = dic[l]

        if d == 'L':
            cs = max(cs+cnt, 0, *list(map(lambda e:cs<=e, wall)))
        elif d == 'R':
            cs = min(cs+cnt, W, *list(map(lambda e:cs>=e, wall)))
        elif d == 'D':
            cs = max(rs+cnt, 0, *list(map(lambda e:rs<=e, wall)))
        elif d == 'R':
            cs = min(cs+cnt, W, *list(map(lambda e:cs>=e, wall)))


if __name__ == '__main__':
    run()
