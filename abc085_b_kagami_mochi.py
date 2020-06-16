def run():
    '''
    N 個の整数 d[0], d[1], ... , d[N-1] が与えられます.
    この中に何種類の異なる値があるでしょうか.

    [制約]
    1≤N≤100
    1≤d[i]≤100
    入力値はすべて整数
    [数値例]
    N = 2
    Q = 3
    d = (8, 10, 8, 6)
    答え : 3
    '''

    # valid when size of list is small enough
    _in = list(map(int, input().split()))
    print(len(set(_in)))

if __name__ == '__main__':
    run()