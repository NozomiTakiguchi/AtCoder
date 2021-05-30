def run(n, k, _in):
    for i in range(n):
        print(_in[i])




if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    _in = [[int(c) for c in input().split()] for _ in range(n)]

    run(n, k, _in)