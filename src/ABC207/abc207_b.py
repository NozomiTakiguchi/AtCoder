
ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    a, b, c, d = na()
    if b >= d*c:
        print(-1)
    else:
        idx = 0
        while (a + b*idx) > d*(c*idx):
            idx += 1
        print(idx)


if __name__ == '__main__':
    run()