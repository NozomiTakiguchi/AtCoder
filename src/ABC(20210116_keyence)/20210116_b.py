import collections
def run(n, k, a):
    '''

    '''
    ans = 0
    N = [0]*n
    counter = collections.Counter(a)

    for e in counter:
        N[e] = counter[e]
    
    for i,e in enumerate(N):
        if e == 0:
            N = N[:i]
            break
    
    print(N)
    _d = {k:v for k,v in enumerate(N)}
    print(_d)

    



    



if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    run(n, k, a)
