ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def dfs(s, _a, result, c):
    if result[s]:
        return


def run():
    n,m = na()
    _a = [[] for _ in range(n)]

    _l = []
    for _ in range(m):
        a, b, c = na()
        _l.append([a,b,c])
        _a[a-1].append(b-1)

    print(_a)
    print(_l)
    for i in range(n):
        for e in _l:
            result = [False]*n
            dfs(e[0]-1, _a, result, e[2])

if __name__ == '__main__':
    run()