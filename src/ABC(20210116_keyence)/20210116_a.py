def run(n, a, b):
    '''

    '''
    _max_a = 0
    _max_b = 0
    prev = 0
    for _a, _b in zip(a, b):
        _max_a = _a if _a > _max_a else _max_a
        ans = _max_a*_b
        prev = ans if ans > prev else prev
        print(prev)

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    run(n, a, b)