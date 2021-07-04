
ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    a, b = na()
    if b < a:
        print('No')
    else:
        print('Yes' if b <= 6*a else 'No')

if __name__ == '__main__':
    run()