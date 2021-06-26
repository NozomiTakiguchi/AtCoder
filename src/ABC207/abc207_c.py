ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    n = ni()
    _i = []
    for _ in range(n):
        _i.append(na())
    l = sorted(_i, key=lambda x: x[1])

    ans = 0
    for iidx,i in enumerate(l):
        _itype, start, end = i
        for jidx, j in enumerate(l):
            _jtype, _s, _e = j
            if jidx <= iidx:
                continue
            if end < _s:
                continue
            if end == _s:
                if _itype in [1,3] and _jtype in [1,2]:
                    ans += 1
                continue
            else:
                ans += 1
    print(ans)

if __name__ == '__main__':
    run()