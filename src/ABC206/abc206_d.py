import sys
sys.setrecursionlimit(500005)

ni = lambda: int(ns())
ns = lambda: input()
na = lambda: list(map(int, input().split()))

upper = [-1]*200001

def root(x):
    if upper[x] < 0:
        return x
    else:
        upper[x] = root(upper[x])
        return upper[x]

def unite(x, y):
    x, y = root(x), root(y)
    if x != y:
        if upper[y] < upper[x]:
            x, y = y, x
        upper[x] += upper[y]
        upper[y] = x
    return x == y


def run():
    n = ni()
    a = na()
    con = 0
    for i in range(n):
        if i < n-1-i:
            if not unite(a[i], a[n-1-i]):
                con += 1
    print(con)
    

if __name__ == '__main__':
    '''
    union find を使って解いている
    '''
    run()