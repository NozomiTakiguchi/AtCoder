if __name__ == '__main__':
    n  = int(input())
    _l = list(map(int, input().split()))

    cnt = 0
    for i in _l:
        if i <= 10:
            continue
        cnt += (i -10)
    print(cnt)

