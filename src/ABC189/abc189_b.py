import collections
def run(n, x, _l):
    '''

    '''
    amount = 0
    for i,e in enumerate(_l):
        if e[1] == 0:
            continue
        amount += (e[0]*e[1])/100
        if amount > x:
            print(i+1)
            exit()
    
    print(-1)
    exit()
if __name__ == '__main__':
    n, x = map(int, input().split())
    _l = [list(map(int, input().split())) for _ in range(n)]


    run(n, x, _l)
