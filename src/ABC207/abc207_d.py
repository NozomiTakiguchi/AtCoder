

ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    n = ni()
    ab = []
    cd = []

    for _ in range(n):
        ab.append(na())
    
    for _ in range(n):
        cd.append(na())


if __name__ == '__main__':
    run()