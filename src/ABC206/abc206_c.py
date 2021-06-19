from collections import defaultdict

def run(n):
    a = list(map(int, input().split()))

    _dic = defaultdict(int)

    for i in a:
        _dic[i] += 1
    
    _len = len(a)
    ans = 0
    for k,v in _dic.items():
        ans += v * (_len - v)
    
    # ↑ で条件を満たす組をちょうど 2 回数えてしまっているため
    print(int(ans/2))





if __name__ == '__main__':
    n = int(input())
    run(n)
