ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    n, k = na()
    q, mod = divmod(k, n)
    a = [(i, e) for i, e in enumerate(na())]
    _a = [(j, *_e) for j,_e in enumerate(sorted(a, key=lambda x:x[1]))]

    a = sorted(_a, key=lambda x:x[1])

    for e in a:
        idx = e[0]
        if idx + 1 <= mod:
            print(q+1)
        else:
            print(q)

if __name__ == '__main__':
    run()