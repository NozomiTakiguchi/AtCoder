def run(n, xy):
    '''

    '''
    _sum = 0
    for _in in xy:
        x,y = _in
        _sum += (x + y)*(y-x+1)/2

    print(int(_sum))

if __name__ == '__main__':
    n = int(input())
    
    xy = [map(int, input().split()) for _ in range(n)]

    run(n, xy)