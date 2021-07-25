_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def _direction(sx, sy, tx, ty):
    assert sx <= tx
    assert sy <= ty
    if tx - sx == 0:
        return 'U' if ty-sy > 0 else 'D'
    else:
        return 'R' if tx-sx > 0 else 'L'





def run():
    print()

if __name__ == '__main__':
    run()