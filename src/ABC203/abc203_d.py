def run(n, k, _in):
    '''
    解説見てもよくわからん.
    2 次元累積和で解くことを考える、とあるので、とりあえず 2 元累積和を解けるようにしておく
    '''
    for i in range(n):
        print(_in[i])




if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    _in = [[int(c) for c in input().split()] for _ in range(n)]

    run(n, k, _in)