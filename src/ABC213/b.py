_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    _a = _l()
    ans = []
    for i,e in enumerate(_a):
        ans.append([i+1,e])
    
    # 大きい順に並べ替えて 2 番目の選手番号を取得
    print(sorted(ans, key=lambda n: n[1], reverse=True)[1][0])


if __name__ == '__main__':
    run()
