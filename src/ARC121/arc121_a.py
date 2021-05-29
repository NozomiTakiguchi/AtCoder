import itertools

def run(n, _l):
    '''

    '''
    prev = 0
    dist = 0
    for e in itertools.combinations(_l, 2):
        a,b = e
        _dist = max([abs(a[0] - b[0]), abs(a[1] - b[1])])
        if _dist <= dist:
            if _dist >= prev:
                prev = _dist
        else:
            dist = _dist
    else:
        print(prev)

if __name__ == '__main__':
    n = int(input())
    _l = [list(map(int, input().split())) for _ in range(n)]

    run(n,_l)