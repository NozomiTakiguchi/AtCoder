import itertools

def run(n):
    '''
    ↓ このアルゴリズムだと例えば
    R 100
    G 1
    B 50
    B 90
    のときに、最小値が 99 になってしまう
    この時のあるべき組み合わせは、 (R100 - B90), (G1 - B50) で、最小値 10 となる

    '''

    def is_odd(n):
        return n%2 != 0
    

    r = []
    r_len = 0
    g = []
    g_len = 0
    b = []
    b_len = 0

    target = []
    # 同じ色の犬が奇数匹のときに _target に追加
    for i in range(2*n):
        e = input().split()
        if e[1] == 'R':
            r.append(e)
            r_len += 1
        elif e[1] == 'G':
            g.append(e)
            g_len += 1
        else:
            b.append(e)
            b_len += 1
    else:
        if is_odd(r_len):
            target.extend(r)
        if is_odd(g_len):
            target.extend(g)
        if is_odd(b_len):
            target.extend(b)
    
    # それぞれの色が偶数匹ずつのとき、不満を感じる犬はいない
    if len(target) == 0:
        print(0)
        exit()

    # かわいさ度の昇順に並べ替える (色は混在)
    _target = sorted(target, key=lambda x: int(x[0]))
    prev_color = _target[0][1]
    prev_cuty  = 0
    cuty_diff = 10**15+10 

    for e in _target:
        if e[1] == prev_color:
            prev_cuty = int(e[0])
            continue

        _cuty = int(e[0])
        _cuty_diff = abs(int(e[0]) - prev_cuty)

        if _cuty_diff <= cuty_diff:
            cuty_diff = _cuty_diff

        prev_color = e[1]
        prev_cuty = int(e[0])

    
    print(cuty_diff)

if __name__ == '__main__':
    n = int(input())
    run(n)