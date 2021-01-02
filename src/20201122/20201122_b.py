def run(_a, _b, _c, _d):
    '''

    '''
    cnt = 0

    diff_1 = _c - _d
    diff_2 = _c + _d

    def dfs(a, b, c, d, cnt):
        if a - b == diff_1:
            return cnt
        elif a + b == diff_2:
            return cnt
        elif abs(a - c) + abs(b - d) <= 3:
            print(cnt)
            exit()
        cnt += 1


if __name__ == '__main__':
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    run(a, b, c, d)