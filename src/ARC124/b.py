_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    a = _l()
    b = set(_l())
    xx = [a[0]^i for i in b] # a1 との xor を調べれば十分

    ans = []
    for x in xx:
        l = set()
        for i in range(n):
            l.add(a[i]^x)
        if l == b: # a xor b = x としたとき a xor x = c で b と c が一致するかどうかを調べる. (https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a より、 a^x^x = a となることを利用する)
            ans.append(x)
    
    ans.sort()
    print(len(ans))
    for a in ans:
        print(a)

if __name__ == '__main__':
    run()
