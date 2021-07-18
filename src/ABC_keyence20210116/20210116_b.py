from collections import defaultdict
_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()


MAX = (10**5)*3

def run():
    n,k = _l()
    _a = sorted(_l())

    dic = defaultdict(int)
    for e in _a:
        dic[e] += 1
    
    ans = 0
    for i in range(MAX):
        k = min(k, dic[i])
        ans += k
    
    print(ans)

if __name__ == '__main__':
    run()