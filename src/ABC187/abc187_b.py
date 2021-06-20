import itertools
def run(n, _list):
    '''

    '''
    cnt = 0
    for e in itertools.combinations(_list, 2):
        i = e[0]
        j = e[1]
        if abs((j[1] - i[1])/(j[0] - i[0])) <= 1:
            cnt += 1
        
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    _list = [list(map(int, input().split())) for _ in range(n)]

    run(n, _list)