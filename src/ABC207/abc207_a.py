

ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    _l = sorted(na(), key=lambda x:x, reverse=True)
    print(sum(_l[:2]))


if __name__ == '__main__':
    run()