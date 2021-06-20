
if __name__ == '__main__':
    n  = int(input())
    _l = list(map(int, input().split()))
    _l.sort(reverse=True)

    max_a = sum(_l)
    ng = -1
    ok = max_a
