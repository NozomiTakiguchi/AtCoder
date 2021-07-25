_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    a,b = _l()
    print(((a-b)/3)+b)

if __name__ == '__main__':
    run()
