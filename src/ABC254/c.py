
def run(n,k,a):

    prev_forth, prev_back = 0,0

    for i in range(n):
        _f,_b = a[i], a[i+k]

        print(_f,_b)
        if _f >= _b:
            _f,_b = _b,_f
            a[i+k] =  _b

        if prev_forth > _f or prev_back > _b:
            print(i,_f,_b, prev_forth, prev_back)

            print('No')
            exit()

        prev_forth, prev_back = _f,_b

    print('Yes')

'''
1: f,b -> 1,3
2: f,b -> 3,4
3: f,b -> 3,4
'''


if __name__ == '__main__':
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    run(n,k,a)