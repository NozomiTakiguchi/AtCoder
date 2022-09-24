def run(x):
    _x = bin(x)[2:]
    ans = '0'.zfill(len(str(_x)))
    l = [True if int(e) else False for e in _x]
    cnt = 2**sum(l)

    for i in range(x):
        _ans = i+1
        





if __name__ == '__main__':
    x = int(input())
    run(x)